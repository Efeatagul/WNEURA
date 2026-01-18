"""
WNEURA NeuroAgent Module
Optimization Date: 2026-01-18
Developer: Efeatagul
Description: Q-Learning agent modulated by biological agency and cortisol levels.
"""

import numpy as np
import sys
import os
import json
from typing import Dict, List, Any, Optional


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from config import BrainConfig
    from brain import BiologicalBrain
except ImportError:
    
    from wneura.config import BrainConfig
    from wneura.brain import BiologicalBrain

class NeuroAgent:
    def __init__(self, action_dim: int, config: BrainConfig, history_limit: int = 1000):
        """
        Nörolojik ajanı başlatır.
        
        Args:
            action_dim (int): Yapılabilecek toplam eylem sayısı.
            config (BrainConfig): Beyin ayarları.
            history_limit (int): Geçmiş verilerin hafızada tutulacağı maksimum adım.
        """
        self.brain = BiologicalBrain(config)
        self.action_dim = action_dim
        self.q_table = np.zeros(action_dim) 
        self.history_limit = history_limit
        
        
        self.history = {
            "rpe": [],
            "q_values": [],
            "actions": [],
            "agency": []
        }

    def act(self, exploration_rate: float = 0.1) -> int:
        """
        Eylem seçer (Epsilon-Greedy Stratejisi).
        Eğer ajan depresyondaysa (Agency=0) keşfetmeyi bırakabilir.
        """
        
        adjusted_exploration = exploration_rate * self.brain.agency
        
        if np.random.rand() < adjusted_exploration:
            return np.random.randint(self.action_dim)
        
        return int(np.argmax(self.q_table))

    def learn(self, action: int, reward: float) -> Dict[str, float]:
        """
        Sonuçlardan öğrenir ve biyolojik parametreleri günceller.
        """
       
        if action >= self.action_dim or action < 0:
            raise ValueError(f"Geçersiz aksiyon indeksi: {action}")

        
        prediction = self.q_table[action]
        delta = reward - prediction 
        
       
        surprise = abs(delta)
        self.brain.update_amygdala(surprise)
        current_agency = self.brain.update_agency(delta)
        
       
        learning_efficacy = self.brain.cfg.base_learning_rate * current_agency
        
        
        self.q_table[action] += learning_efficacy * delta
        
        
        self._update_history(delta, action, current_agency)
        
        return {
            "rpe": float(delta),
            "agency": float(current_agency),
            "cortisol": float(self.brain.cortisol),
            "learning_efficacy": float(learning_efficacy),
            "q_value": float(self.q_table[action])
        }

    def _update_history(self, rpe, action, agency):
        """Yardımcı Fonksiyon: Geçmişi kaydeder ve belleği temizler."""
        self.history["rpe"].append(float(rpe))
        self.history["actions"].append(int(action))
        self.history["agency"].append(float(agency))
       
        if len(self.history["rpe"]) > self.history_limit:
            self.history["rpe"].pop(0)
            self.history["actions"].pop(0)
            self.history["agency"].pop(0)

    def save_state(self, filepath: str):
        """Ajanın beynini ve öğrendiklerini JSON olarak kaydeder."""
        state = {
            "q_table": self.q_table.tolist(),
            "brain_state": {
                "agency": self.brain.agency,
                "cortisol": self.brain.cortisol,
                "amygdala": self.brain.amygdala
            }
        }
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=4)
        print(f"✅ Beyin durumu kaydedildi: {filepath}")

    def load_state(self, filepath: str):
        """Kaydedilmiş bir beyni geri yükler."""
        if not os.path.exists(filepath):
            print(f"⚠️ Dosya bulunamadı: {filepath}")
            return
            
        with open(filepath, 'r') as f:
            state = json.load(f)
            
        self.q_table = np.array(state["q_table"])
        self.brain.agency = state["brain_state"]["agency"]
        self.brain.cortisol = state["brain_state"]["cortisol"]
        self.brain.amygdala = state["brain_state"]["amygdala"]
        print(f"♻️ Beyin durumu geri yüklendi: {filepath}")


if __name__ == "__main__":
    print("🧪 Agent Modülü Test Ediliyor...", flush=True)
    
    try:
       
        cfg = BrainConfig()
        agent = NeuroAgent(action_dim=2, config=cfg)
        print(f"✅ Başlatma Başarılı. Agency: {agent.brain.agency}")
        
        
        act = agent.act()
        info = agent.learn(act, reward=10)
        print(f"✅ Öğrenme Başarılı. RPE: {info['rpe']:.2f}")
        
      
        agent.save_state("test_brain_dump.json")
        
     
        if os.path.exists("test_brain_dump.json"):
            os.remove("test_brain_dump.json")
            print("✅ Temizlik yapıldı.")
            
    except Exception as e:
        print(f"❌ HATA: {e}")
