from dataclasses import dataclass

@dataclass
class BrainConfig:
    cortisol_decay: float = 0.95
    amygdala_gain: float = 0.5
    base_learning_rate: float = 0.1
    gamma: float = 0.95
    initial_agency: float = 1.0
    stress_threshold: float = 0.6
    erosion_rate: float = 0.05
    repair_rate: float = 0.01
    mastery_threshold: float = 0.1

    def summary(self):
        print(self.erosion_rate > self.repair_rate)
        print(self.stress_threshold)