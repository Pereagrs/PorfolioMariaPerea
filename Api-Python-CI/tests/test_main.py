from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hola, María! Esta es mi API desde FastAPI."}

def test_suma():
    r = client.get("/suma?a=3&b=4")
    assert r.status_code == 200
    assert r.json() == {"result": 7}
