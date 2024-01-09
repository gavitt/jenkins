# test_app.py

import pytest

from app import app  # Импортируйте app из вашего основного файла


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_pytest(client):
    """Тест главной страницы с использованием фикстуры pytest"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Привет, мир!'
