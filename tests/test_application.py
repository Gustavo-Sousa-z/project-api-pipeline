import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Gustavo",
            "last_name": "Sousa",
            "cpf": "892.244.030-93",
            "email": "gustavo.sousa@teste.com.br",
            "birth_date": "1998-08-04"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "João",
            "last_name": "Santos",
            "cpf": "242.753.346-24",
            "email": "Joao.Santos@testedois.com",
            "birth_date": "1924-21-52"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "Gustavo"
        assert response.json[0]["last_name"] == "Sousa"
        assert response.json[0]["cpf"] == "892.244.030-93"
        assert response.json[0]["email"] == "gustavo.sousa@teste.com.br"

        birth_date = response.json[0]["birth_date"]["$date"]
        assert birth_date == "1998-08-04T00:00:00Z"

        response = client.get('/user/%s' % invalid_user["cpf"])
        assert response.status_code == 400
        assert b"User does not exist in database!" in response.data
