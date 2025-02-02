"""
(1) Training Evaluation criteria: 
    - Tailoring evaluation to the application: accuracy, recall, BLEURT, ROUGE, PERPLEXITY, etc
    - The emergence of LLMs as judges: like human alignment
        + Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (https://arxiv.org/abs/2306.05685)

    - Consistency and diversity in test sets

(2) Production evaluation and monitoring
    - Live Experiment and Gradual Rollout: Increasing a small increasingly samples to student model and monitoring how the application metrics are changed before running a mass samples.
    - Dark Launch: keep the teacher and student on production and evaluate whether the gap is. But the student model routes on background. 
        => shadow deployment
    - Hybrid Launch: if the teacher model outperforms the student, navigate/control which tasks are implemented by 
        => blue-green deployment

    - Output monitoring: by rule-based or other LLMs and logs for other enhancement later
        
"""