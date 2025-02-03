"""
    1) Annotated data platform: Argilla
        - 
    2) Llama 3.1 series: as auto-generated based entity name label
        - Using Hugging Face Inference Endpoints/API that reduced the hosting/serving cost.
       Replaced by chatGPT endpoints
"""


def test(input):
    from gliner import GLiNER
    strURL = "EmergentMethods/gliner_small_news-v2.1"
    labels = ["person", "location", "date", "event", "facility", "vehicle", "number", "organization","thing"]

    model = GLiNER.from_pretrained(strURL)

    entities = model.predict_entities(input, labels, threshold=0.5)

    for ent in entities:
        print(f"{ent['text']} => {ent['label']} ")




if __name__ == "__main__":
    print("Hello EFTP worlds")
    test("""EMCOR Group Company Awarded Contract for Installation of Process Control Systems for Orange County Water District's Water Purification Facilities updated at Feb, 2025""")