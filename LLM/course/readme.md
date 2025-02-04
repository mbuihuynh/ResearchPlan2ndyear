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

ELECTRA: discriminate sampled token vs. real token means that "Efficiently Learning an Encoder that Classifies Token Replacements Accurately"

- SSL: during pre-train stage, network can see MASK tokens which are corrupted
- Finetune on downstream tasks: network discriminate which tokens are samples or real => downstream task is discrimination task

=> network can learn all input tokens insteading of subset tokens like MLM used in BERT approach.
