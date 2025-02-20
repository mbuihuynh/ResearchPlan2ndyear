"""
    Purpose: fine-tune BERT/ELECTRA (encoder-only models, bi-directional context) for specified tasks in Vietnamese language
        - Sentiment Analysis
        - Text summary
        Stage-1: self-supervised learning with MLM - %k masked token strategy
        Stage-2: downstream task fine-tuning
    => we need the medium-size model with efficient computation
    Methods: distillation techniques

ELECTRA
Stage-1:
    SSL task: replace some tokens by some ones sampled from a small generator network => train a model to discriminate real token or generated samples
 
"""