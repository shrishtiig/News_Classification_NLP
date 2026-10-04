from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_news

app = FastAPI()


class NewsArticle(BaseModel):
    title: str
    description: str


@app.get("/")
def home():
    return {"message": "News Classification API is working!"}


@app.post("/predict")
def predict(article: NewsArticle):
    prediction = predict_news(
        article.title,
        article.description
    )

    return {
        "prediction": prediction
    }