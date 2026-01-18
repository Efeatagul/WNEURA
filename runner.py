"""
WNEURA HEADLESS RUNNER v1.2
Optimization Date: 2026-01-18
Developer: Efeatagul

Description:
    Bu script, WSharp (C#) veya Terminal üzerinden WNEURA motorunu tetikler.
    Parametreleri alır, simülasyonu koşturur ve sonucu JSON olarak basar.
"""

import argparse
import json
import os
import sys
import numpy as np


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from wneura.config import BrainConfig
    from wneura.agent import NeuroAgent
except ImportError:
    
    from config import BrainConfig
    from agent import NeuroAgent

def parse_arguments():
    parser = argparse.ArgumentParser(description="WNEURA Neuro-Simulation CLI")
    
    
    parser.add_argument('--steps', type=int, default=100, help='Simülasyon adım sayısı')
    parser.add_argument('--scenario', type=str, default='mixed', choices=['mixed', 'chaos', 'therapy', 'stable'], help='Ortam senaryosu')
    parser.add_argument('--output', type=str, default='simulation_result.json', help='Çıktı JSON dosyası')
    
   
    parser.add_argument('--erosion', type=float, default=0.05, help='Agency aşınma hızı')
    parser.add_argument('--repair', type=float, default=0.01, help='Agency onarım hızı')
    parser.add_argument('--stress_threshold', type=float, default=0.6, help='Kortizol tetik eşiği')
    parser.add_argument('--initial_agency', type=float, default=1.0, help='Başlangıç iradesi')
    
    return parser.parse_args()

def get_environment_reward(scenario):
    """Senaryoya göre ödül/ceza üretir."""
    if scenario == 'chaos':
        return np.random.randint(-5, 0) 
    elif scenario == 'therapy':
        return 5 
    elif scenario == 'stable':
        return 0 
    else:
        return np.random.randint(-5, 5)

def main():
    args = parse_arguments()
    print(f"🚀 WNEURA ENGINE STARTED. Steps: {args.steps}, Scenario: {args.scenario}")
    
    try:
        
        cfg = BrainConfig()
        cfg.erosion_rate = args.erosion
        cfg.repair_rate = args.repair
        cfg.stress_threshold = args.stress_threshold
        cfg.initial_agency = args.initial_agency
        
       
        agent = NeuroAgent(action_dim=1, config=cfg)
        
     
        history = {
            "step": [],
            "cortisol": [],
            "agency": [],
            "rpe": [],
            "action": []
        }
        
    
        for t in range(args.steps):
            
            action = agent.act()
            
        
            reward = get_environment_reward(args.scenario)
            
           
            info = agent.learn(action, reward)
        

            history["step"].append(t)
            history["cortisol"].append(float(info["cortisol"]))
            history["agency"].append(float(info["agency"]))
            history["rpe"].append(float(info["rpe"]))
            history["action"].append(int(action))

           
            if args.steps >= 10 and t % (args.steps // 10) == 0:
                progress = (t / args.steps) * 100
                print(f"   ... Progress: {int(progress)}%", flush=True)

       
        output_data = {
            "status": "success",
            "parameters": vars(args),
            "final_stats": {
                "final_agency": history["agency"][-1],
                "final_cortisol": history["cortisol"][-1]
            },
            "timeline": history
        }
        print("✅ Simulation completed successfully.")

    except Exception as e:
    
        print(f"❌ CRITICAL ERROR: {str(e)}")
        output_data = {
            "status": "error",
            "error_message": str(e),
            "parameters": vars(args)
        }

 
    try:
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=4)
        print(f"💾 Results saved to: {args.output}")
    except Exception as e:
        print(f"❌ COULD NOT WRITE FILE: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
