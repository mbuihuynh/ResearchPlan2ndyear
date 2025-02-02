"""
- Purpose: 1) bootstrap the dataset with synthetic data so that generated samples produced are varied/diversified and non-repetitive, cleased
           2) Maximize the quality of your training data

- Refer to 
(1) Synthetic data
    Self-Instruct: seed query to chatGPT
    - Self-Instruct: Aligning Language Models with Self-Generated Instructions
    - https://arxiv.org/pdf/2310.14558

    Phi 1/1.5
    https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/

    Textbooks Are All You Need II: phi-1.5 technical report, https://arxiv.org/pdf/2309.05463

(2) Qualifying data
    - Common techniques:
        + Manually fix or curate your data
        + Filter data based on rules.
        + Rank your data with auxiliary systems (https://arxiv.org/abs/2107.04512)
        + Enrich data with explanation traces: Collect reasoning data, chain-of-thought (CoT) outputs from the teacher.
        + Aggregate your teachers: 
            + chaining: https://blog.langchain.dev/fine-tuning-chatgpt-surpassing-gpt-4-summarization/
            + Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine: https://arxiv.org/abs/2311.16452

(3) How much enough data is for fine-tuning
    Depending specified tasks + training parameters that need a small/large dataset (at least 10K samples???)
    Tools
        + Conduct the dataset (size varies) + parameters ablation studies
        + Data augmentation as text-attact - Generating adversarial examples for ablation studies (https://github.com/QData/TextAttack)
            => can understand the model
                

"""


