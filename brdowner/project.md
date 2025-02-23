# Enhanced LLMs to Products/Services Management

### **Papers**

- Fino1: On the Transferability of Reasoning-Enhanced LLMs to Finance (https://arxiv.org/pdf/2502.08127)
  - https://github.com/The-FinAI/Fino1
- HuatuoGPT-o1 (https://arxiv.org/pdf/2412.18925) guide the strategy to generate the reasoning path data
- FinNLP-FNP-LLMFinLegal-2025 Shared Task: Regulations Challenge (https://aclanthology.org/2025.finnlp-1.42.pdf)

### **Duration**: *max 6 months*


---

# **** SOLUTION ****

---



## I. Accurated Datasets

#### a. BRDQA (Priority 1)

- Business requirement document in HTML/ Confluence pages: text + figures
- 5K open-ended question - answer pair from sources
  - Jira tickets
  - Generation Q&A process: we trust the large closed multi reasoning models like GPT o1, o3-mini-high

#### b. DOCMATH (Priority 2)

**Reference paper:** Evaluating Math Reasoning Capabilities of LLMs in Understanding Long and Specialized Documents (https://arxiv.org/pdf/2311.09805)

#### c. XBRL-Math (Priority 2)

Reference paper: FinNLP-FNP-LLMFinLegal-2025 Shared Task: Regulations Challenge (https://aclanthology.org/2025.finnlp-1.42.pdf)

#### d. Reasoning Path Generation (Priority 1)

- Verifier agent: the reasoning model GPT-4o
- Following the sampling strategy from HuatuoGPT-o1
  - (1) Backtracking - Revisiting
  - (2) Exploring New Paths
  - (3) Verification - Cross checking
  - (4) Correction

# II. Model Training

#### 1. Backbone

- Select the backbone Llama 3x.8B Instruct

#### 2. Finetune Proces

#### *Pre-trainging*

- Qwen 2 pretrained on a large datasets: different sizes: 0.5B, 1.5B, 7B, 72B. That uses MoE mechanism as Mistral.AI + support 30 languages + a big token vocabulary 151, 642

##### 2.a Pretraining as Knowledge Distillation

- Distill Llama 3.2 8B Instruct to Llama 3.2-SPPO 4B follows as https://developer.nvidia.com/blog/llm-model-pruning-and-knowledge-distillation-with-nvidia-nemo-framework/



#### *Post-Training*

##### 2.b. SFT (supervised finetuning) phase

- Use the curated dataset: X = {question}, Y = {reasoning path and final answer}
- Model to learn the structured financial reasoning
- Setup:
  - base learning rate: 5e-6
  - max. seq length: 8192
  - epoch: 3
  - LoRA to efficient update parameters

##### 2.c. Preference learning phase

- Model to learn the quality of generated reasoning path
- Optimizer: PPO - Proximal Policy Optimization + Verifier agent process
- Setup:
  - base learning rate: 5e-7
  - epoch: 3
  - The reward model is utilized by HuatuoGPT-o1

---

# **** PLAN  ****

- Release prototype and basecode in 4 sprints

---

#### S116 ([from date]    -> [end date]): Pre-training | KB phase

- Prepare datasets as the acquired KB pipeline under csv format
- Basecode for knowledge distillation pretrain

#### S117 ([from date]    -> [end date]): Post-training | Data Preparation

- Experiment for KB phase
- Prepare dataset of reasoning path generation

#### S118 ([from date]    -> [end date]): Post-training | SFT + PPO

#### S119 ([from date]    -> [end date]): Codebase for Prototype
