import matplotlib.pyplot as plt
import numpy as np
from config import BrainConfig
from agent import NeuroAgent

def run_dissociation_experiment():
    print("DENEY 2: Uncertainty vs Helplessness")
    
    cfg_healthy = BrainConfig()
    cfg_healthy.erosion_rate = 0.0 
    agent_healthy = NeuroAgent(action_dim=1, config=cfg_healthy)
    
    cfg_helpless = BrainConfig()
    cfg_helpless.initial_agency = 0.01 
    agent_helpless = NeuroAgent(action_dim=1, config=cfg_helpless)
    
    logs = {"healthy_q": [], "helpless_q": []}
    
    for t in range(100):
        reward_healthy = np.random.randint(-5, 6) 
        agent_healthy.act()
        agent_healthy.learn(0, reward_healthy)
        
        reward_helpless = 2
        agent_helpless.act()
        agent_helpless.learn(0, reward_helpless)
        
        logs["healthy_q"].append(agent_healthy.q_table[0])
        logs["helpless_q"].append(agent_helpless.q_table[0])

    plt.figure(figsize=(10, 6))
    plt.plot(logs["healthy_q"], color="green", alpha=0.7)
    plt.plot(logs["helpless_q"], color="red", linewidth=3)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_dissociation_experiment()