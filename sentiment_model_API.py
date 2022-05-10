from fastapi import FastAPI
from transformers import pipeline
from transformers import AutoTokenizer
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
token = AutoTokenizer.from_pretrained("blanchefort/rubert-base-cased-sentiment", model_max_length=100)
classifier = pipeline("sentiment-analysis", model = "blanchefort/rubert-base-cased-sentiment", tokenizer=token)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text, truncation=True)[0]
