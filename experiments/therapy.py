"""
WNEURA THERAPY SIMULATION v1.2
Optimization Date: 2026-01-18
Developer: Efeatagul

Description:
    Bu modül, travma sonrası stres bozukluğu (PTSD) ve iyileşme (Rehabilitation)
    süreçlerini simüle eder. Hysteresis etkisini (kalıcı hasar) test eder.
"""

import numpy as np
import sys
import os
import json


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from wneura.config import BrainConfig
    from wneura.agent import NeuroAgent
except ImportError:
   
    from config import BrainConfig
    from agent import NeuroAgent

def run_therapy_session(repair_speed=0.01, experiment_name="Standard", save_log=False):
    print(f"\n{'='*60}")
    print(f"🧪 EXPERIMENT: {experiment_name} | Repair Rate: {repair_speed}")
    print(f"{'='*60}")
    
    
    cfg = BrainConfig()
    cfg.initial_agency = 1.0        
    cfg.repair_rate = repair_speed  
    
    
    agent = NeuroAgent(action_dim=1, config=cfg)
    
    
    history = {"step": [], "agency": [], "cortisol": [], "phase": []}


    print("\n🔻 [PHASE 1] Trauma Induction (Chaotic Environment)")
    print("   Ortam: Rastgele Negatif Ödüller (Belirsizlik)")
    
    for t in range(40):
        action = agent.act()
        reward = np.random.randint(-5, 0) 
        info = agent.learn(action, reward)
        
     
        history["step"].append(t)
        history["agency"].append(info["agency"])
        history["cortisol"].append(info["cortisol"])
        history["phase"].append("Trauma")

        if t % 10 == 0:
            print(f"   Step {t}: Agency={info['agency']:.2f}, Cortisol={info['cortisol']:.2f}")

    print(f"   >> Post-Trauma Agency: {info['agency']:.2f}")

   
    print("\n🟢 [PHASE 2] Therapy Session (Supportive Environment)")
    print("   Ortam: Sabit Pozitif Ödüller (Güven)")

    for t in range(40):
        action = agent.act()
        reward = 5 
        info = agent.learn(action, reward)
        
       
        history["step"].append(t + 40)
        history["agency"].append(info["agency"])
        history["cortisol"].append(info["cortisol"])
        history["phase"].append("Therapy")

        if t % 10 == 0:
            print(f"   Step {t+40}: Agency={info['agency']:.2f}")

   
    final_agency = info['agency']
    print(f"\n🏁 [RESULT] Final Agency = {final_agency:.2f}")
    
    status = "UNKNOWN"
    if final_agency > 0.8:
        status = "FULL RECOVERY (Tam İyileşme)"
        print(f"   ✅ STATUS: {status}")
    elif final_agency > 0.4:
        status = "PARTIAL RECOVERY (Kısmi İyileşme)"
        print(f"   ⚠️ STATUS: {status}")
    else:
        status = "FAILED - CHRONIC DEPRESSION (Hysteresis Effect)"
        print(f"   ❌ STATUS: {status}")


    if save_log:
        filename = f"therapy_result_{experiment_name.lower().replace(' ', '_')}.json"
        output_data = {
            "experiment": experiment_name,
            "parameters": {"repair_rate": repair_speed},
            "result": status,
            "final_stats": {"agency": final_agency},
            "timeline": history
        }
        with open(filename, 'w') as f:
            json.dump(output_data, f, indent=4)
        print(f"   💾 Log saved to: {filename}")

if __name__ == "__main__":

    run_therapy_session(repair_speed=0.01, experiment_name="Natural Recovery", save_log=True)
    
   
    run_therapy_session(repair_speed=0.05, experiment_name="Enhanced Therapy", save_log=True)
