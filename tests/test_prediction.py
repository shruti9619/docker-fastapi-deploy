from fastapi.testclient import TestClient
from docker_fastapi_deploy.main import app

client = TestClient(app)


def test_predict():
    response = client.post("/predict", json={"data": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert response.json() == {"prediction": 0}
