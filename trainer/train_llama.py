#### Env: docker exec -it sklearn-gpu-3 /bin/bash
####        torch2 environment
# Common libs
import pandas as pd

# LLM libs 
import torch
from trl import SFTTrainer 
from transformers import TrainingArguments
from unsloth.chat_templates import get_chat_template
from unsloth import FastLanguageModel
from datasets import Dataset
from unsloth import is_bf16_supported
from transformers import AutoTokenizer, AutoModelForSequenceClassification

"""
1. framework: unsloth
Common: specified optimize the performance as enhance speed, reduce memory consumption, evaluate accuracy
- Efficient: Unsloth + QLoRA adapter
- Attention Mechanism: integrate Flash-Attention
- Causal Mask for Speed: apply causal mask for speeding up training

2. framework: trl
purpose: post-train language as SFT, DPO

"""

def train(db_filename_json):
    data = pd.read_json(db_filename_json,lines=True)


    print(data.head(5))

    




if __name__ == "__main__":
    print("Hello MBui")
    json_file = "data_sets/mentalhealthconversations/combined_dataset.json"
    train(db_filename_json=json_file)