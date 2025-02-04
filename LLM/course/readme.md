# Course

- COS 597G (Fall 2022): Understanding Large Language Models (https://www.cs.princeton.edu/courses/archive/fall22/cos597G/)
- CS 886: Recent Advances on Foundation Models Winter 2024 (https://cs.uwaterloo.ca/~wenhuche/teaching/cs886/)


# I. What are LLMs?

### Recommended reading

- BERT: encoder only models
- T5: encoder - decoder models
- GPT3: decoder only models

### a. Encoder-only models

BERT: SSL task: %k masking token and predict the masked token.

RoBERTa (A Robustly Optimized BERT Pretraining Approach)

ELECTRA: discriminate sampled token vs. real token means that "Efficiently Learning an Encoder that Classifies Token Replacements Accurately"

- Pretrain stage: alternatively, SSL use MLM as BERT, Electra use two models generator <-> discriminator in SSL
  - generator is trained to generate the real token
  - discriminator is trained to classify whether token is real or generated
  - generator network is a small model using MLM technique: randomly mask %K token in an input x. [MASK] token replaced by a set of selected positions and then generator is trained to predict the original token masked.
  - a total of loss = L_{MLM} (x, \theta_G) +   \lambda * L_{disc} (x,\theta_D)
- Finetune stage: discriminator network is used to fine-tune the downstream task
- Notes for experiments
  - Weight sharing: D & G network are shared weights at embedding layer => it calls as tied token embedding between two models G & D.
- **How to train the two models**
  - Only train G with L_{MLM} for n-steps
  - Initialize the weight of D with the weights of G. Then train D with L_{disc} for n-steps while till keeping the G's weight frozen.

=> network can learn all input tokens insteading of subset tokens like MLM used in BERT approach.

### b. Encoder - decoder models

T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

Problem: treating each problem in NLP as text-to-text task => Author proposed the framework as Text-to-Text Transfer Transformation.



AlexaTM 20B: Few-shot Learning Using a Large-Scale Multilingual Seq2Seq Model
