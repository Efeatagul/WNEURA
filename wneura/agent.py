import numpy as np
from config import BrainConfig
from brain import BiologicalBrain

class NeuroAgent:
    def __init__(self, action_dim: int, config: BrainConfig):
        self.brain = BiologicalBrain(config)
        self.q_table = np.zeros(action_dim) 
        self.action_dim = action_dim
        self.history = {
            "rpe": [],
            "q_values": [],
            "actions": []
        }

    def act(self, exploration_rate=0.1):
        if np.random.rand() < exploration_rate:
            return np.random.randint(self.action_dim)
        return np.argmax(self.q_table)

    def learn(self, action, reward):
        prediction = self.q_table[action]
        delta = reward - prediction 
        
        surprise = abs(delta)
        self.brain.update_amygdala(surprise)
        
        current_agency = self.brain.update_agency(delta)
        
        learning_efficacy = self.brain.cfg.base_learning_rate * current_agency
        
        self.q_table[action] += learning_efficacy * delta
        
        self.history["rpe"].append(delta)
        self.history["q_values"].append(self.q_table.copy())
        self.history["actions"].append(action)
        
        return {
            "rpe": delta,
            "agency": current_agency,
            "cortisol": self.brain.cortisol,
            "learning_efficacy": learning_efficacy
        }