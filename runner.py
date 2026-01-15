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
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--erosion', type=float, default=0.05)
    parser.add_argument('--repair', type=float, default=0.01)
    parser.add_argument('--stress_threshold', type=float, default=0.6)
    parser.add_argument('--initial_agency', type=float, default=1.0)
    parser.add_argument('--steps', type=int, default=100)
    parser.add_argument('--output', type=str, default='simulation_result.json')
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    print(f"WNEURA ENGINE STARTED. Steps: {args.steps}")
    
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
        reward = np.random.randint(-5, 3) 
        
        info = agent.learn(action, reward)
        
        history["step"].append(t)
        history["cortisol"].append(float(info["cortisol"]))
        history["agency"].append(float(info["agency"]))
        history["rpe"].append(float(info["rpe"]))
        history["action"].append(int(action))

    print(f"Saving results to: {args.output}")
    
    output_data = {
        "status": "success",
        "parameters": vars(args),
        "final_stats": {
            "final_agency": history["agency"][-1],
            "final_cortisol": history["cortisol"][-1]
        },
        "timeline": history
    }
    
    with open(args.output, 'w') as f:
        json.dump(output_data, f, indent=4)
        
    print("DONE.")

if __name__ == "__main__":
    main()
