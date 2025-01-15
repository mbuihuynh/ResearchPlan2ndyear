
```
POLlaMA: Building Open-source Language Model for Product Owner
==============
```

- Applying the training process from the work PMC_LlaMA. There are two stages: data centric knowledge injection which enrich knowledge into LLM and PO soecified instuction tuning stage to align with PO use-case
- The text input as a sequence of tokens, learning objective is minimize auto-regressive loss

#### Confluence website:

- Langchain's ConfluenceLoader with TextSplitter, TokenSplitter to efficiently split the document into text snippets
- LlamaIndex: **from** llama_index**.**readers**.**confluence **import** ConfluenceReader


#### Training setup:

##### Stage 1: injecting knowledge

- Loss: auto-regression loss
- Context length size = 2048
- Batch size: 3200
- optmizer: AdamW => replace LiOn
- 1 epoch: must see all tokens, max-epoch = 5
- Fully Sharded Data Parallel (FSDP) acceleration strategy, bf16 (Brain Floating Point) data format, and gradient checkpointing

###### Github:

- https://huggingface.co/blog/ImranzamanML/fine-tuning-1b-llama-32-a-comprehensive-article
- https://www.datacamp.com/tutorial/fine-tuning-llama-3-2

##### Stage 2: instruction tuning

- Supervised Fine Tuning: Applying the method of knowledge distillation
