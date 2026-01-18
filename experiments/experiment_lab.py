"""
WNEURA GRAND EXPERIMENT v1.0
The Unified Simulation: Structure (Brain) + Chemistry (NeuroModulator)
Developer: Efeatagul

Senaryo:
    1. The Hustle (Adım 0-30): Yüksek Stres, Yüksek Ödül (Başarı bedel ister).
    2. The Burnout (Adım 30-60): Stres devam eder, ödüller kesilir (Çöküş).
    3. The Recovery (Adım 60-90): Düşük Stres, Düzenli Ödül (Rehabilitasyon).
"""

import time
import sys
import os
import numpy as np


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from wneura.config import BrainConfig
    from wneura.agent import NeuroAgent
    from neuromodulator import NeuroChemistry 
except ImportError:
    from config import BrainConfig
    from agent import NeuroAgent
    from neuromodulator import NeuroChemistry

def print_header():
    print(f"\n{'='*100}")
    print(f"{'STEP':<5} | {'PHASE':<15} | {'CORTISOL (Stress)':<20} | {'AGENCY (Will)':<20} | {'DOPAMINE':<15} | {'RECEPTOR':<10}")
    print(f"{'-'*100}")

def draw_bar(value, max_val=1.0, color_char="█", length=15):
    """ASCII bar çizer"""
    normalized = min(max(value, 0), max_val) / max_val
    filled = int(normalized * length)
    return (color_char * filled).ljust(length, '░')

def run_grand_experiment():
    
    print("⚙️  Initializing Biological Systems...")
    
  
    cfg = BrainConfig()
    cfg.stress_threshold = 0.5
    cfg.erosion_rate = 0.05
    cfg.repair_rate = 0.02
    
    agent = NeuroAgent(action_dim=1, config=cfg) 
    chem = NeuroChemistry()                      
    
    print_header()
    
 
    total_steps = 90
    phase_name = "START"
    
    for t in range(total_steps):
        
       
        reward = 0
        stress_input = 0.0
        
        if t < 30:
            phase_name = "THE HUSTLE "
            
            reward = np.random.randint(2, 8) 
            stress_input = np.random.uniform(0.1, 0.4) 
            
        elif t < 60:
            phase_name = "BURNOUT "
           
            reward = np.random.randint(-5, 0)
            stress_input = np.random.uniform(0.5, 0.9)
            
        else:
            phase_name = "RECOVERY "
           
            reward = 3
            stress_input = 0.0

      
        action = agent.act()
    
        info = agent.learn(action, reward)
        
       
        agent.brain.update_amygdala(stress_input)
        
   
        chem_state = chem.update(
            reward_signal=reward, 
            stress_signal=info['cortisol'], 
            action_taken=True
        )

       
        cortisol_val = info['cortisol']
        agency_val = info['agency']
        dopamine_val = chem_state['effective_dopamine']
        receptor_val = chem_state['receptor_health']
        
      
        c_bar = draw_bar(cortisol_val, 1.0, "▓")
        a_bar = draw_bar(agency_val, 1.0, "█")
        
        
        d_bar = f"{dopamine_val:.2f}" 
        r_bar = f"{receptor_val:.2f}"

       
        print(f"{t:<5} | {phase_name:<15} | {c_bar} {cortisol_val:.2f} | {a_bar} {agency_val:.2f} | {d_bar:<15} | {r_bar:<10}")
        
       
        time.sleep(0.05)

    print(f"{'='*100}")
    print(" DENEY SONUCU ANALİZİ:")
    print(f"   • Final Agency: {agency_val:.2f} (İrade)")
    print(f"   • Final Receptor Health: {receptor_val:.2f} (Dopamin Duyarlılığı)")
    
    if receptor_val < 0.8:
        print("    UYARI: Reseptör hasarı (Tolerans) tespit edildi. Ajan 'Bağımlılık' döngüsüne girmiş olabilir.")
    if agency_val < 0.2:
        print("    UYARI: Agency çöküşü (Depresyon) tespit edildi.")
    else:
        print("    SİSTEM: Ajan zorluklara rağmen hayatta kaldı.")

if __name__ == "__main__":
    run_grand_experiment()
