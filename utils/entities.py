from dataclasses import dataclass

@dataclass
class LLMQueryLog:
    input: str
    output: str

    #metadata
    timestamp: int
    input_tokens: int
    output_tokens: int
    duration: int
    model: str
    temperature: float
    max_tokens: int


