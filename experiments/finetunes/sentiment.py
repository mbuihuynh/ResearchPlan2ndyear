"""
    URLs: https://www.datacamp.com/tutorial/fine-tuning-llama-3-2

"""
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, TextStreamer


def load_checkpoints(checkpoint):
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)

    model = AutoModelForCausalLM.from_pretrained(
        checkpoint,return_dict = True
        , low_cpu_mem_usage=True, torch_dtype = torch.float16
        , device_map = "auto",
        trust_remote_code = True
    )

    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    
    if model.pad_token_id is None:
        model.config.pad_token_id = model.config.eos_token_id 


    return {
        'tokenizer' : tokenizer,
        'model' : model
    }

def run():
    pass




if __name__ == "__main__":
    checkpoint = "/Users/mai.bui/.llama/checkpoints/Llama3.2-3B"

    dict_models = load_checkpoints(checkpoint)

    print(dict_models['model'])
