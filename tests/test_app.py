"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_account_creation(client: FlaskClient):
    # Test creating an account
    response = client.post('/accounts/testuser')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'testuser'

def test_get_account(client: FlaskClient):
    # Create account first
    client.post('/accounts/testuser2')
    # Retrieve account
    response = client.get('/accounts/testuser2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'testuser2'

def test_get_account_not_found(client: FlaskClient):
    response = client.get('/accounts/nonexistent')
    assert response.status_code == 404


