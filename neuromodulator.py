"""
WNEURA NEUROMODULATOR SYSTEM v1.0
Scientific Base: Neurochemistry & Receptor Dynamics
Developer: Efeatagul

Description:
    Bu modül, sinaptik iletimi ve nörotransmitter dengesini simüle eder.
    Dopamin (DA), Serotonin (5-HT) ve Noradrenalin (NE) seviyelerini ve
    reseptör duyarlılığını (Downregulation/Upregulation) yönetir.
"""

import numpy as np
import time

class NeuroChemistry:
    def __init__(self):
        
        self.dopamine = 1.0      
        self.serotonin = 1.0      
        self.norepinephrine = 1.0 

        
        self.da_receptors = 1.0
        self.ht_receptors = 1.0
        self.ne_receptors = 1.0

        print("🧪 [CHEMISTRY] Synaptic gaps initialized.")

    def update(self, reward_signal, stress_signal, action_taken):
        """
        Her adımda kimyasal dengeyi günceller.
        """
        
        if reward_signal > 0:
            self.dopamine += 0.2 * reward_signal
        else:
            self.dopamine -= 0.1 

       
        if stress_signal > 0.5:
            self.serotonin -= 0.05 * stress_signal
        elif action_taken:
            self.serotonin += 0.02

       
        target_ne = 1.0 + (stress_signal * 1.5)
        self.norepinephrine += (target_ne - self.norepinephrine) * 0.1

       
        self._apply_homeostasis()
        
       
        self._update_receptors()

        return self.get_state()

    def _apply_homeostasis(self):
        """Kimyasallar zamanla 1.0 (Baseline) seviyesine dönmeye çalışır (Reuptake)."""
        decay = 0.05
        self.dopamine += (1.0 - self.dopamine) * decay
        self.serotonin += (1.0 - self.serotonin) * decay
       
        self.norepinephrine += (1.0 - self.norepinephrine) * (decay * 0.5)

    def _update_receptors(self):
        """
        Tolerans Yasası:
        Çok fazla kimyasal = Reseptör ölümü (Downregulation)
        Çok az kimyasal = Reseptör artışı (Upregulation)
        """
        adaptation_rate = 0.01

        
        if self.dopamine > 1.5:
            self.da_receptors -= adaptation_rate 
        elif self.dopamine < 0.8:
            self.da_receptors += adaptation_rate 
        
        
        self.da_receptors = np.clip(self.da_receptors, 0.5, 1.5)

    def get_state(self):
        """Efektif (Hissedilen) seviyeleri döndürür."""
        
        return {
            "effective_dopamine": self.dopamine * self.da_receptors,
            "effective_serotonin": self.serotonin * self.ht_receptors,
            "effective_norepinephrine": self.norepinephrine * self.ne_receptors,
            "receptor_health": self.da_receptors
        }


if __name__ == "__main__":
    chem = NeuroChemistry()
    print("\n--- 🧠 CHEMICAL IMBALANCE SIMULATION (High Dopamine Injection) ---")
    print(f"{'STEP':<6} | {'DOPAMINE (DA)':<20} | {'RECEPTOR (Sens)':<15} | {'EFFECT':<10}")
    print("-" * 60)

    
    for t in range(30):
        
        state = chem.update(reward_signal=5.0, stress_signal=0.2, action_taken=True)
        
        
        da_bar = "█" * int(chem.dopamine * 5)
        rc_bar = "▒" * int(chem.da_receptors * 10)
        
        print(f"{t:<6} | {da_bar:<20} | {rc_bar:<15} | {state['effective_dopamine']:.2f}")
        time.sleep(0.05)

    print("\n🔻 SONUÇ: Dopamin tavan yapmasına rağmen, 'Receptor' azaldığı için")
    print("         'Effect' (Hissedilen Haz) aynı oranda artmadı. İşte TOLERANS budur.")
