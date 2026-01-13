import numpy as np
import json
import os
from datetime import datetime
from config import BrainConfig

class BiologicalBrain:
    """
    WNEURA CORE ENGINE v1.1 (Industrial Grade)
    
    Bu sınıf, ajan davranışlarını yöneten biyolojik durum makinesidir.
    HPA Ekseni (Stres), Striatum (Öğrenme) ve Agency (İrade) dinamiklerini simüle eder.
    
    Yetenekler:
    - Leaky Integrator Stres Modeli
    - Hysteresis Tabanlı Agency Çöküşü
    - Homeostatik Direnç (Active Resistance)
    - JSON Tabanlı Durum Kaydı (Persistence)
    """

    def __init__(self, config: BrainConfig):
        
        if config.erosion_rate <= config.repair_rate:
            print("UYARI: Erosion Rate, Repair Rate'den düşük. Hysteresis oluşmayabilir!")

        self.cfg = config
        
       
        self._cortisol = 0.0             
        self._agency = config.initial_agency
        
        
        self._resistance = 1.0            
        
        
        self.history = {
            "timestamp": [],
            "cortisol": [],
            "agency": [],
            "delta_agency": [],
            "resistance": []
        }
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] WNEURA Brain Initialized. Agency: {self._agency}")

    @property
    def cortisol(self):
        """Kortizol seviyesini okur (Read-Only)"""
        return self._cortisol

    @property
    def agency(self):
        """Agency seviyesini okur (Read-Only)"""
        return self._agency

    def _calculate_homeostasis(self):
        """
        [DAHİLİ METOD] Homeostatik Direnç Hesabı.
        Sürekli stres altındaysan vücut direnci düşer (Burnout).
        """
        if self._cortisol > 0.8:
        
            self._resistance *= 0.99
        else:
            
            self._resistance += 0.01
        
        self._resistance = np.clip(self._resistance, 0.5, 1.5)

    def update_amygdala(self, surprise_signal: float) -> float:
        """
        Kortizol Dinamikleri (Denklem 2.2 + Homeostasis)
        Girdi: Surprise (Beklenti Hatası)
        Çıktı: Güncel Kortizol Seviyesi
        """
        
        self._calculate_homeostasis()
        
       
        effective_gain = self.cfg.amygdala_gain / self._resistance
        synthesis = effective_gain * surprise_signal
        
       
        self._cortisol = (self._cortisol * self.cfg.cortisol_decay) + synthesis
        
        
        self._cortisol = np.clip(self._cortisol, 0.0, 1.0)
        
        return self._cortisol

    def update_agency(self, rpe: float) -> float:
        """
        Agency Dinamikleri (Denklem 2.3 - Hysteresis Core)
        Girdi: RPE (Reward Prediction Error)
        Çıktı: Güncel Agency Seviyesi
        """
        
        stress_gap = self._cortisol - self.cfg.stress_threshold
        erosion_factor = 0.0
        
        if stress_gap > 0:
            
            erosion_factor = self.cfg.erosion_rate * (stress_gap ** 2) * 5.0
        
      
        repair_factor = 0.0
        if rpe > self.cfg.mastery_threshold:
            repair_factor = self.cfg.repair_rate
        
       
        d_agency = repair_factor - erosion_factor
        self._agency += d_agency
        
        
        self._agency = np.clip(self._agency, 0.0, 1.0)
        
        
        self._log_state(d_agency)
        
        return self._agency

    def _log_state(self, delta_agency):
        """Dahili loglama sistemi"""
        self.history["timestamp"].append(datetime.now().isoformat())
        self.history["cortisol"].append(float(self._cortisol))
        self.history["agency"].append(float(self._agency))
        self.history["delta_agency"].append(float(delta_agency))
        self.history["resistance"].append(float(self._resistance))

    def get_learning_modulator(self) -> float:
        """Striatum modülasyon sinyali"""
        return self._agency

   
    
    def save_brain_state(self, filename="brain_dump.json"):
        """Beynin o anki tüm kimyasını diske kaydeder."""
        state = {
            "cortisol": self._cortisol,
            "agency": self._agency,
            "resistance": self._resistance,
            "config": self.cfg.__dict__ 
        }
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)
        print(f"Brain state saved to {filename}")

    def load_brain_state(self, filename="brain_dump.json"):
        """Diskteki beyin yedeğini geri yükler."""
        if not os.path.exists(filename):
            print("Save file not found.")
            return
            
        with open(filename, 'r') as f:
            state = json.load(f)
            
        self._cortisol = state["cortisol"]
        self._agency = state["agency"]
        self._resistance = state.get("resistance", 1.0)
        print(f"Brain state loaded. Agency restored to: {self._agency}")
