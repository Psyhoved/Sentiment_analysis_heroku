from fastapi.testclient import TestClient
from sentiment_model_API import app

client = TestClient(app)

def test_read_sentiment_model_API():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}