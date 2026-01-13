import matplotlib.pyplot as plt
import numpy as np
from config import BrainConfig
from agent import NeuroAgent

def run_contingency_experiment():
    print("DENEY 3: Contingency Switch")
    
    cfg_healthy = BrainConfig()
    cfg_healthy.initial_agency = 1.0
    cfg_healthy.repair_rate = 0.0 
    agent_healthy = NeuroAgent(action_dim=1, config=cfg_healthy)
    
    cfg_helpless = BrainConfig()
    cfg_helpless.initial_agency = 0.0 
    cfg_helpless.repair_rate = 0.01 
    agent_helpless = NeuroAgent(action_dim=1, config=cfg_helpless)
    
    logs = {"healthy_q": [], "helpless_q": []}
    
    for t in range(100):
        if t < 50:
            reward = 0.1 
        else:
            reward = 10.0 
            
        agent_healthy.act() 
        agent_healthy.learn(0, reward) 
        
        agent_helpless.act() 
        agent_helpless.learn(0, reward) 
        
        logs["healthy_q"].append(agent_healthy.q_table[0])
        logs["helpless_q"].append(agent_helpless.q_table[0])

    plt.figure(figsize=(10, 6))
    plt.axvline(x=50, color="black", linestyle="--")
    plt.plot(logs["healthy_q"], color="green", linewidth=2)
    plt.plot(logs["helpless_q"], color="red", linewidth=3)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_contingency_experiment()