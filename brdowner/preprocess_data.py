"""
    Purpose: download html pages in Confluence
        Project: SmartPOS
        Pro-processing steps
            - Removing HTML tags
            - Detecting text in english and ignore Vietnamese text
            - Identify a whole sentence based on punctual mark.

        Output: json file (it should be similar to data format in wikitext-103-v1)
            {"text": " = Homarus gammarus = \n"} => category
            {"text": " == Homarus gammarus == \n"} => category
            {"text": "content \n"}

"""

import json
import os
from datasets import load_dataset
import html2text
from langdetect import detect
from abc import ABC, abstractmethod
from copy import deepcopy

class doAction(ABC):
    @abstractmethod
    def __call__(self, *args, **kwds):
        pass

class doHTML2Text(doAction):
    def __init__(self):
        super().__init__()
        self.h = html2text.HTML2Text()

    def __call__(self, text) -> str:
        return self.h.handle(text)
    
class doLang(doAction):
    def __init__(self,lang:list):
        super().__init__()
        vocab_lang = ['af', 'ar', 'bg', 'bn', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'fa', 'fi', 'fr', 'gu', 'he']
        vocab_lang = vocab_lang + ['hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv', 'mk', 'ml', 'mr', 'ne', 'nl', 'no', 'pa', 'pl']
        vocab_lang = vocab_lang + ['pt', 'ro', 'ru', 'sk', 'sl', 'so', 'sq', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'zh-cn', 'zh-tw']
        assert lang, "Need to select the langs"
        assert set(vocab_lang).union(set(lang)), 'Make sure that your selected langs in supported libs %s' . format(vocab_lang)
        self.cf_lang = lang

    def __call__(self, text) -> str:
        predicted = detect(text)
        if predicted in self.cf_lang:
            return text
        
        return None

class doFormat(doAction):
    pass

class doDetectSentence(doAction):
    """
        Output: list
    """
    def __call__(self, text) -> list:
        pass


class PreprocessText():
    def __init__(self, pipeline:list):
        self.pipeline = pipeline

    def process(self,text):
        
        original_text = deepcopy(text)
        for action in self.pipeline:
            text = action(text)


        return {
            'original' : original_text,
            'output' : text
        }
        
        



def download_confluence():
    pass



def _get_wiki_data():
    dataset = load_dataset("wikitext", "wikitext-103-v1")

    data_folder = 'data_sets/wikitext-data'
    os.makedirs(data_folder, exist_ok=True)
    
    # Define file paths and destination paths
    file_paths = {
        'train': os.path.join(data_folder, 'wikitext-train.jsonl'),
        'validation': os.path.join(data_folder, 'wikitext-val.jsonl'),
        'test': os.path.join(data_folder, 'wikitext-test.jsonl')
    }
    
    # Function to save dataset split to a JSONL file
    def save_to_jsonl(file_path, data):
        with open(file_path, 'w') as file:
            for item in data:
                file.write(json.dumps(item) + '\n')
    
    # Define splits
    splits = ["train", "validation", "test"]
    
    # Save splits to JSONL files and calculate their sizes
    for split in splits:
        if split in dataset:
            save_to_jsonl(file_paths[split], dataset[split])
        else:
            print(f"Split {split} not found in the dataset.")


if __name__ == "__main__" :
    print("Hello")
    _get_wiki_data()