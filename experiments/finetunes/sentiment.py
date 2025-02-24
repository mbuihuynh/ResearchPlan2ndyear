"""
    URLs: https://www.datacamp.com/tutorial/fine-tuning-llama-3-2

"""
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, TextStreamer
from huggingface_hub import login


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

    login(token=)

    model_id = "meta-llama/Llama-3.2-3B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    messages = [
        {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
        {"role": "user", "content": "Who are you?"},
    ]
    outputs = pipe(
        messages,
        max_new_tokens=256,
    )
    print(outputs[0]["generated_text"][-1])




if __name__ == "__main__":
    checkpoint = "/Users/mai.bui/.llama/checkpoints/Llama3.2-3B"

    # dict_models = load_checkpoints(checkpoint)
    # print(dict_models['model'])

    run()
