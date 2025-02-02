"""
    Training strategy:
        - Beside mostly approaches as exploring like
            + experiment different teacher foundation models
            + test precision vs. quantization
            + training hyper-parameters

        - Curriculum learning: the model is fine-tuned through multi-stages
        Per stage of (Paper: Orca 2: Teaching Small Language Models How to Reason)
            + different kind of training data: quality, size, noise, in/out domain
            + different complexity level: basic/concept -->> specified/complex 
        RLHF/RLAIF/DPO: is to fine-tune on "preference tuning" / human preferences

"""