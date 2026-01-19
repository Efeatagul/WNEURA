"""
WNEURA HIPPOCAMPAL MEMORY SYSTEM v1.0
Scientific Base: Synaptic Tagging & Capture (STC) Hypothesis
Developer: Efeatagul

Description:
    Bu modül, ajanın kısa ve orta süreli hafızasını yönetir.
    Her olayı kaydetmek yerine, "Duygusal Ağırlığı" (Emotional Weight)
    yüksek olan olayları önceliklendirir.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class MemoryTrace:
    """Tek bir anı parçasını temsil eden veri yapısı."""
    step_id: int           
    state: Any             
    action: int           
    reward: float          
    surprise: float         
    cortisol: float        
    
  
    importance: float = 0.0 

class Hippocampus:
    def __init__(self, capacity: int = 50, decay_rate: float = 0.05):
        """
        Args:
            capacity: Hafızada tutulabilecek maksimum olay sayısı.
            decay_rate: Anıların her adımda ne kadar silikleşeceği.
        """
        self.capacity = capacity
        self.decay_rate = decay_rate
        self.memories: List[MemoryTrace] = []
        
     
        print("🧠 [HIPPOCAMPUS] Memory buffer initialized inside 'wneuraa'.")

    def encode_experience(self, step, state, action, reward, surprise, cortisol):
        """
        Duygusal Etiketleme (Amygdala-Hippocampal Tagging).
        Anının önemini hesaplar ve eğer değerliyse saklar.
        """
   
        emotional_weight = abs(surprise) + (cortisol * 1.5)
        
        if emotional_weight < 0.1:
            return
        
        new_memory = MemoryTrace(
            step_id=step,
            state=state,
            action=action,
            reward=reward,
            surprise=surprise,
            cortisol=cortisol,
            importance=emotional_weight
        )
        
        self.memories.append(new_memory)
        self._manage_capacity()

    def decay_memories(self):
        """Zamanın geçmesiyle anıların silikleşmesi."""
        for mem in self.memories:
            mem.importance *= (1.0 - self.decay_rate)
        
        self.memories = [m for m in self.memories if m.importance > 0.05]

    def _manage_capacity(self):
        """Hafıza dolarsa, en ESKİYİ değil, en ÖNEMSİZİ siler."""
        if len(self.memories) > self.capacity:
            self.memories.sort(key=lambda m: m.importance)
            excess = len(self.memories) - self.capacity
            self.memories = self.memories[excess:]

    def get_replay_batch(self, batch_size=5):
        """Rüya modu için en güçlü anıları getirir."""
        sorted_mem = sorted(self.memories, key=lambda m: m.importance, reverse=True)
        return sorted_mem[:batch_size]


if __name__ == "__main__":
    print("🔬 Hippocampus Test Başlatılıyor...")
    hippo = Hippocampus()
    print("✅ Hippocampus sınıfı başarıyla oluşturuldu.")
    
    
    hippo.encode_experience(1, [0,0], 1, 10, 5.0, 0.8)
    print(f"✅ Anı eklendi. Hafıza durumu: {len(hippo.memories)} anı var.")
