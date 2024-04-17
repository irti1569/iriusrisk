from unittest.mock import patch

import pytest

import iriusrisk.views
from run import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_summary_okay(client):

    response = client.post("/summarize", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json['summary'] == "hello"
