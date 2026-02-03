from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def testar_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def testar_soma_correta():
    response = client.get("/soma?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 8}

def testar_soma_negativa():
    response = client.get("/soma?a=-2&b=-2")
    assert response.status_code == 200
    assert response.json() == {"resultado": -4}