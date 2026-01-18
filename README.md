# 🧠 WNEURA v1.2: Multi-Dimensional Cognitive Simulation Platform

![WSharp](https://img.shields.io/badge/WSharp-Native_Architecture-%23512BD4?style=for-the-badge&logo=c-sharp&logoColor=white)
![Python](https://img.shields.io/badge/Python-100%25-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Phase%202%20Ready-success?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Neuroscience%20%26%20Bio--AI-purple?style=for-the-badge)

**Status:** Phase 2 (Bridge System & Neurochemistry Ready) 🌉  
**Field:** Computational Neuroscience / Neurochemistry / Bio-Inspired AI  
**Integration:** Optimized for WSharp (C#) & External Control  

WNEURA is a neuroscience-focused platform designed to simulate biological brain development, neurochemical balances, and decision-making processes within a multi-dimensional digital environment.

**Version 1.2** introduces a **"Neurochemical Modulation" (Dopamine/Serotonin)** layer and transitions to a **"Headless"** engine architecture, enabling full integration with external software (specifically WSharp) via JSON protocols.
     
---

## 🛠️ Core Engine Architecture

The platform operates through the mathematical integration of two primary layers: **Structural** and **Chemical**.

### 1. Structural Layer (The Brain)
| Mechanism | Analog | Function |
| :--- | :--- | :--- |
| **Amygdala** | Stress Engine | Generates Cortisol based on prediction errors (Surprise). |
| **Agency ($W$)** | Volition Weight | Manages the belief in causality between action and outcome. |
| **Striatum** | Learning Gate | Stops learning (Freezing) if Agency is too low, even if a reward is present. |

### 2. Chemical Layer (Neurochemistry) - *New in v1.2*
| Neurotransmitter | Domain | Simulation Mechanism |
| :--- | :--- | :--- |
| **Dopamine (DA)** | Motivation & Reward | Simulates receptor sensitivity (Tolerance) and addiction cycles. |
| **Serotonin (5-HT)** | Mood Stability | Suppressed by stress; replenished by successful action. |
| **Noradrenaline (NE)** | Focus (Arousal) | Affects performance based on the Yerkes-Dodson law. |

---

## 📂 Project Structure

The project is organized into core engine components and experimental scenarios:

```text
WNEURA/
├── wneura/                  # Core Package
│   ├── __init__.py          # Package initializer
│   ├── agent.py             # Neurological Agent (Decision Maker)
│   ├── brain.py             # Biological Engine (Cortisol/Agency Dynamics)
│   ├── neuromodulator.py    # Chemistry Lab (Dopamine/Receptor) 🧪
│   ├── config.py            # Hyperparameters
│   └── runner.py            # CLI & C# Bridge Commander
│
├── experiments/             # Scenarios & Tests
│   ├── experiment_lab.py    # The Grand Experiment (Burnout Sim) 📉
│   └── therapy.py           # Rehabilitation Tests
│
└── README.md                # Documentation
```
🔌 Integration & Usage
To trigger the WNEURA engine externally (via Terminal or WSharp), use runner.py.

1. Standard Simulation (CLI)
```
py wneura/runner.py --steps 100 --scenario chaos --output result.json
```
2. The Grand Experiment (Burnout Lab) 🔥
```
py experiments/experiment_lab.py
```
This command launches a live biological dashboard with ASCII graphics in the terminal.

Validation Experiments
The biological accuracy of the model has been proven through four fundamental experiments:

1. Hysteresis Proof (Permanent Damage)
It has been proven that even if stress (Cortisol) is removed, the Agency level does not recover spontaneously.
```
Observation: Post-trauma, the system remains locked in "Helplessness" mode.
```
2. Contingency Switch (Opportunity Blindness)
Even when a massive reward (+10) is introduced to the environment, the helpless agent fails to notice this opportunity and cannot update its motivation (Outcome Insensitivity).

3. Therapy & Rehabilitation
Tested via experiments/therapy.py.
```
Observation: Giving standard rewards to an agent with zeroed Agency (Agency=0) is ineffective. The system only begins to respond when the "Repair Rate" is increased via external support (simulating medication or intense therapy).
```
4. Receptor Downregulation (Tolerance & Addiction) - New
Tested via experiments/experiment_lab.py.
```
Observation: During "The Hustle" phase (High Stress + High Reward), although dopamine levels skyrocket, Receptor Sensitivity decreases. Consequently, the agent cannot derive satisfaction even from rewards, eventually leading to Burnout.
```
📈 Experimental Results
```
Experiment      File / Visual                           Status
Hysteresis	    results/figure_01_hysteresis.png	    Successful ✅
Dissociation	results/figure_02_dissociation.png	    Successful ✅
Contingency	    results/figure_03_contingency.png	    Successful ✅
Therapy Sim	    experiments/therapy.py (Log)	        Successful ✅
Burnout Lab	    experiments/experiment_lab.py (Live)    Successful ✅
```
🗺️ Future Roadmap
```
[x] Phase 1: Core Engine & Validation (Completed)
[x] Phase 2: Headless Architecture & JSON Bridge (Completed)
[x] Phase 2.5: Neurochemistry & Receptor Dynamics (Completed) 🧪
[ ] Phase 3: Full WSharp (C#) Integration and UI.
[ ] Phase 4: Multi-Agent Interaction (Social Helplessness).
```
Developer: [Efeatagul]
License: MIT License. Open for scientific use and development.
