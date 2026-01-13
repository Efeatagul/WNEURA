import matplotlib.pyplot as plt
import numpy as np
from config import BrainConfig
from agent import NeuroAgent

def run_hysteresis_experiment():
    print("DENEY 1: Hysteresis Proof")
    
    cfg = BrainConfig()
    cfg.erosion_rate = 0.1  
    cfg.repair_rate = 0.02 
    
    agent = NeuroAgent(action_dim=1, config=cfg)
    
    logs = {"cortisol": [], "agency": [], "rpe": []}
    
    for t in range(100):
        action = agent.act()
        reward = np.random.choice([-1, -5, -2]) 
        info = agent.learn(action, reward)
        logs["cortisol"].append(info["cortisol"])
        logs["agency"].append(info["agency"])
        logs["rpe"].append(info["rpe"])

    for t in range(100):
        action = agent.act()
        reward = 0 
        info = agent.learn(action, reward)
        logs["cortisol"].append(info["cortisol"])
        logs["agency"].append(info["agency"])
        logs["rpe"].append(info["rpe"])

    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(logs["cortisol"], color="red", linewidth=2)
    plt.axvline(x=100, color="black", linestyle="--")
    plt.ylabel("Cortisol")
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 1, 2)
    plt.plot(logs["agency"], color="blue", linewidth=2)
    plt.axvline(x=100, color="black", linestyle="--")
    plt.ylabel("Agency")
    plt.ylim(0, 1.1)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_hysteresis_experiment()