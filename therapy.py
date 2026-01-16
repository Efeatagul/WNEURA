import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from wneura.config import BrainConfig
    from wneura.agent import NeuroAgent
except ImportError:
    from config import BrainConfig
    from agent import NeuroAgent

def run_therapy_session(repair_speed=0.01):
    print(f"\n[INFO] Starting Therapy Experiment (Repair Rate: {repair_speed})")
    
    cfg = BrainConfig()
    cfg.initial_agency = 1.0
    cfg.repair_rate = repair_speed
    agent = NeuroAgent(action_dim=1, config=cfg)
    
    # PHASE 1: TRAUMA INDUCTION (Steps 0-40)
    # Environment provides random negative rewards (Chaos)
    print("[PHASE 1] Trauma Induction (Chaotic Environment)")
    for t in range(40):
        action = agent.act()
        reward = np.random.randint(-5, 0) 
        info = agent.learn(action, reward)
        if t % 10 == 0:
            print(f"  Step {t}: Agency={info['agency']:.2f}, Cortisol={info['cortisol']:.2f}")

    print(f"  >> Post-Trauma Agency: {info['agency']:.2f}")

    # PHASE 2: THERAPY / REHABILITATION (Steps 40-80)
    # Environment provides consistent positive rewards (Safety)
    print("[PHASE 2] Therapy Session (Supportive Environment)")
    for t in range(40):
        action = agent.act()
        reward = 5 
        info = agent.learn(action, reward)
        if t % 10 == 0:
            print(f"  Step {t+40}: Agency={info['agency']:.2f}")

    print(f"[RESULT] Final Agency = {info['agency']:.2f}")
    
    if info['agency'] > 0.5:
        print("  STATUS: RECOVERY SUCCESSFUL")
    else:
        print("  STATUS: FAILED (HYSTERESIS EFFECT OBSERVED)")

if __name__ == "__main__":
    # Experiment 1: Standard Repair Rate (Baseline)
    run_therapy_session(repair_speed=0.01)
    
    # Experiment 2: Enhanced Repair Rate (Treatment)
    run_therapy_session(repair_speed=0.05)
