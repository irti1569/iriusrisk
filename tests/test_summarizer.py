
import pytest

from run import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_summary(client):

    response = client.post("/summarize", json={"text": "hello"})
    assert response.status_code == 200
