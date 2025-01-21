```
==============
A Survey on RAG Meeting LLMs
==============
```

The paper link at 
- https://dl.acm.org/doi/10.1145/3637528.3671470
- https://advanced-recommender-systems.github.io/RAG-Meets-LLMs/

![RAG Paper Cites STATS](image/RAG/cites_stats.png)

***LLMs architectures***
- From Encoder (BERT): bi-directional encoder => well-understand the context/semantic of words => good at sentiment analysis, conversation/dialog
- From Decoder (GPT families): is trained on auto-regression => text generation
- From Encoder-Decoder (T5): complex text generation problems

*Limitations of RAG*
- Hallucinations: incorrectly factual problem, non-sensical, misleading information.

# Retrieval - Augmented Large Langugage Models (RA-LLMs)

Example of framework RAG-LLMs in QA task
![RA-LLM Framework Examples](image/RAG/LLMs_RA.png)

There are three components:
### Retrieval: dense vs sparse retrieval
- dense retrieval: word/BoW/TF-IDF/BM25 => compact meaning 
- sparse retrieval: indexing => haviely storage => searching faster.
![retrieval_components](image/RAG/retrieval_components.png)
- Retrieval Results:
    - chunk results: passages
    - token results: fast queries + apply in cases of rare pattern or out-of-domain

- Strategy: pre / post
    - Pre-retrieval: enhancing query by generating pseudo-document/ hypothetical document/ rewrite the query with more conducive questions
        - queries expansion (Query2doc)
        - HyDE method: Hypothetical Document Embedding
        - rewrite query: clarify the retrieval need in the new query
        - *query augmentation*: combine original query and preliminary generated outputs as a new query => retrieve relevant information from the external database => **good strategy of the query enhancement**.
    - Post-retrieval: process the extracted top-k documents from retriever before feeding them into generator
        - Retrieve-Rerank-Generate ($R^2$ G) => ranking the retrieved documents from the different retrieval approaches => boosting the robustness of the retrieval results
    - Fixing the preventing long retrieved documents => compress the retrieved documents into a smaller document/summary
        - Retrieve, Compress, Prepend (RECOMP) => add model/intermediate layers to transform the retreived documents into textual summary before feeding into the generation process.
        - FiD (Exploring the Multi-document Reader for Prompt Compression)
- Database:
    - Option key-value: keys for similarity matching (likely sparse vectors for BM25 or dense embeddings from retrieval encoding); value mostly is raw-text.

### Generation:

### Augmentation: augmented at the layers of input / output / middle


