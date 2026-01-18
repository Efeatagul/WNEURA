"""
WNEURA Configuration Module
Optimization Date: 2026-01-18
Developer: Efeatagul
Description: Nörolojik simülasyonun tüm hiperparametrelerini yönetir.
"""

from dataclasses import dataclass, asdict
import json
import os

@dataclass
class BrainConfig:
    
    cortisol_decay: float = 0.95    
    amygdala_gain: float = 0.5     
    stress_threshold: float = 0.6  
    
    
    base_learning_rate: float = 0.1 
    gamma: float = 0.95            
    
   
    initial_agency: float = 1.0    
    erosion_rate: float = 0.05     
    repair_rate: float = 0.01       
    mastery_threshold: float = 0.1 

    def to_dict(self):
        """Ayarları sözlük (dictionary) formatına çevirir."""
        return asdict(self)

    def save_to_json(self, filename="config.json"):
        """Ayarları dosyaya kaydeder (WSharp okusun diye)."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
        print(f"⚙️ Config saved to {filename}")

    @classmethod
    def load_from_json(cls, filename="config.json"):
        """Dosyadan ayar yükler (WSharp ayar gönderirse diye)."""
        if not os.path.exists(filename):
            print(f"⚠️ Config file not found: {filename}. Using defaults.")
            return cls() 
        
        with open(filename, 'r') as f:
            data = json.load(f)
        
        
        valid_keys = {k: v for k, v in data.items() if k in cls.__annotations__}
        print(f"⚙️ Config loaded from {filename}")
        return cls(**valid_keys)

    def summary(self):
        """Ayarların kısa bir özetini ve uyarıları basar."""
        print("\n--- BRAIN CONFIGURATION ---")
        for key, value in self.to_dict().items():
            print(f" • {key}: {value}")
        
      
        if self.erosion_rate <= self.repair_rate:
            print("⚠️ [WARNING] Erosion Rate <= Repair Rate.")
            print("   Simülasyonda 'Kalıcı Hasar' (Hysteresis) oluşmayabilir!")
            print("   Tavsiye: Erosion Rate, Repair Rate'den en az 2-3 kat büyük olmalı.")
        else:
            print("✅ [OK] Hysteresis dynamics active.")
        print("---------------------------\n")


if __name__ == "__main__":
    cfg = BrainConfig()
    cfg.summary()
  
