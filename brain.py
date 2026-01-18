"""
WNEURA CORE ENGINE v1.2 (Optimized)
Optimization Date: 2026-01-18
Developer: Efeatagul

Description:
    Biyolojik durum makinesi. HPA Ekseni (Stres), Striatum (Öğrenme) 
    ve Agency (İrade) dinamiklerini simüle eder.
"""

import numpy as np
import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, Optional


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from config import BrainConfig
except ImportError:
    
    print("⚠️ UYARI: 'config.py' bulunamadı. Varsayılan ayarlar kullanılıyor.")
    class BrainConfig:
        pass

class BiologicalBrain:
    def __init__(self, config: Any, history_limit: int = 1000):
        """
        Biyolojik motoru başlatır.
        
        Args:
            config: Ayar nesnesi (BrainConfig).
            history_limit: RAM koruması için tutulacak maksimum log sayısı.
        """
        self.cfg = config
        self.history_limit = history_limit
        
        
        self.amygdala = 0.0 
        
       
        self._cortisol = 0.0             
        self._agency = getattr(config, 'initial_agency', 1.0) 
        self._resistance = 1.0  
        
        
        erosion = getattr(config, 'erosion_rate', 0.0)
        repair = getattr(config, 'repair_rate', 0.0)
        if erosion > 0 and repair > 0 and erosion <= repair:
            print(f"⚠️ DİKKAT: Erosion ({erosion}) <= Repair ({repair}). Hysteresis oluşmayabilir!")

       
        self.history = {
            "timestamp": [],
            "cortisol": [],
            "agency": [],
            "delta_agency": [],
            "resistance": []
        }
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 🧠 WNEURA Brain Initialized. Agency: {self._agency:.2f}")

    @property
    def cortisol(self) -> float:
        """Kortizol seviyesini okur (Read-Only)"""
        return self._cortisol

    @property
    def agency(self) -> float:
        """Agency seviyesini okur (Read-Only)"""
        return self._agency

    def _calculate_homeostasis(self):
        """
        [DAHİLİ] Homeostatik Direnç Hesabı.
        Sürekli stres (Kortizol > 0.8) direnci kırar (Burnout).
        """
        if self._cortisol > 0.8:
            self._resistance *= 0.99 
        else:
            self._resistance += 0.01 
        
       
        self._resistance = np.clip(self._resistance, 0.5, 1.5)

    def update_amygdala(self, surprise_signal: float) -> float:
        """
        Kortizol Dinamikleri (Denklem 2.2 + Homeostasis).
        """
        self._calculate_homeostasis()
        
        
        self.amygdala = float(surprise_signal)
        
       
        amygdala_gain = getattr(self.cfg, 'amygdala_gain', 0.1)
        cortisol_decay = getattr(self.cfg, 'cortisol_decay', 0.9)

      
        effective_gain = amygdala_gain / self._resistance
        synthesis = effective_gain * surprise_signal
        
    
        self._cortisol = (self._cortisol * cortisol_decay) + synthesis
        self._cortisol = np.clip(self._cortisol, 0.0, 1.0)
        
        return self._cortisol

    def update_agency(self, rpe: float) -> float:
        """
        Agency Dinamikleri (Denklem 2.3 - Hysteresis Core).
        """
        
        stress_threshold = getattr(self.cfg, 'stress_threshold', 0.5)
        erosion_rate = getattr(self.cfg, 'erosion_rate', 0.01)
        mastery_threshold = getattr(self.cfg, 'mastery_threshold', 0.1)
        repair_rate = getattr(self.cfg, 'repair_rate', 0.02)

       
        stress_gap = self._cortisol - stress_threshold
        erosion_factor = 0.0
        
        if stress_gap > 0:
            
            erosion_factor = erosion_rate * (stress_gap ** 2) * 5.0
        
        
        repair_factor = 0.0
        if rpe > mastery_threshold:
            repair_factor = repair_rate
        
       
        d_agency = repair_factor - erosion_factor
        self._agency += d_agency
        
        
        self._agency = np.clip(self._agency, 0.0, 1.0)
        
       
        self._log_state(d_agency)
        
        return self._agency

    def _log_state(self, delta_agency):
        """Geçmişi kaydeder ve RAM şişmesini önler."""
        self.history["timestamp"].append(datetime.now().isoformat())
        self.history["cortisol"].append(float(self._cortisol))
        self.history["agency"].append(float(self._agency))
        self.history["delta_agency"].append(float(delta_agency))
        self.history["resistance"].append(float(self._resistance))

       
        if len(self.history["timestamp"]) > self.history_limit:
            for key in self.history:
                self.history[key].pop(0)

    def save_brain_state(self, filename="brain_dump.json"):
        """Beynin kimyasını kaydeder (Persistence)."""
        state = {
            "cortisol": self._cortisol,
            "agency": self._agency,
            "resistance": self._resistance,
            "amygdala": self.amygdala
        }
        try:
            with open(filename, 'w') as f:
                json.dump(state, f, indent=4)
            print(f"✅ Brain state saved: {filename}")
        except Exception as e:
            print(f"❌ Save Error: {e}")

    def load_brain_state(self, filename="brain_dump.json"):
        """Beynin kimyasını geri yükler."""
        if not os.path.exists(filename):
            print(f"⚠️ Load file not found: {filename}")
            return
            
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
                
            self._cortisol = state.get("cortisol", 0.0)
            self._agency = state.get("agency", 0.5)
            self._resistance = state.get("resistance", 1.0)
            self.amygdala = state.get("amygdala", 0.0)
            print(f"♻️ Brain state loaded. Agency: {self._agency}")
        except Exception as e:
            print(f"❌ Load Error: {e}")
