from fastapi.testclient import TestClient
from sentiment_model_API import app

client = TestClient(app)


def test_read_sentiment_model_API():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_predict_positive():
    response = client.post("/predict/",
                           json={"text": "Я люблю машинное обучение!"}
                           )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_read_predict_negative():
    response = client.post("/predict/",
                           json={"text": "Я ненавижу машинное обучение!"}
                           )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'

def test_read_predict_neutral():
    response = client.post("/predict/",
                           json={"text": "Mашинное обучение это нормально."}
                           )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'NEUTRAL'

