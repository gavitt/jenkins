# test_app.py

import pytest
from flask_testing import TestCase

from app import app  # Импортируйте app из вашего основного файла


class MyTest(TestCase):

    def create_app(self):
        # Создание экземпляра тестового клиента вашего приложения Flask
        app.config['TESTING'] = True
        return app

    def test_home(self):
        # Отправляем HTTP GET запрос на главную страницу и проверяем результат
        response = self.client.get('/')
        # проверяем, что статус-код ответа равен 200
        self.assertEqual(response.status_code, 200)
        # проверяем что тело ответа соответствует ожидаемому
        self.assertEqual(response.data.decode('utf-8'), 'Привет, мир!')

# Фикстура pytest для упрощения доступа к тестовому клиенту Flask


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_pytest(client):
    """Тест главной страницы с использованием фикстуры pytest"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Привет, мир!'
