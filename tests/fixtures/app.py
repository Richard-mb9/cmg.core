import pytest
from flask import Flask
from flask.testing import FlaskClient
from dotenv import find_dotenv, load_dotenv
from src.app import create_app
from src.security.Auth import Auth
from src.config import Base, get_engine


class Client(FlaskClient):
    def __init__(self, app):
        super().__init__(app)
        self.token_data = {
            'id': 1,
            'email': 'teste@teste.com',
            'roles': []
        }

    def get(self, path: str, headers = {}, use_token = True):
        if headers == {} and use_token:
            headers = {'access_token': self.__generate_token()}
        return super().get(path, headers=headers)
    
    def post(self, path: str, data, headers = {}, use_token = True):
        if headers == {} and use_token:
            headers = {'access_token': self.__generate_token()}
        return super().post(path,data=data, headers=headers)
    
    def put(self, path: str, data, headers = {}, use_token = True):
        if headers == {} and use_token:
            headers = {'access_token': self.__generate_token()}
        return super().put(path,data=data, headers=headers)
    
    def delete(self, path: str, headers = {}, use_token = True):
        if headers == {} and use_token:
            headers = {'access_token': self.__generate_token()}
        return super().delete(path, headers=headers)

    def roles(self, roles):
        if isinstance(roles, str):
            self.token_data['roles'] = [roles]
        if isinstance(roles, list):
            self.token_data['roles'] = roles
        return self
    
    def user_id(self, user_id):
        self.token_data['id'] = user_id
        return self

    def email(self, user_email):
        self.token_data['email'] = user_email
        return self

    def __generate_token(self):
        return Auth().generateToken(self.token_data)


@pytest.fixture(scope='session')
def app():
    env = find_dotenv('.env.test')
    load_dotenv(env)
    Base.metadata.create_all(bind=get_engine())
    app = create_app()

    yield app
    import os
    os.remove('file.db')

    
@pytest.fixture
def app_context(app: Flask):
    with app.app_context() as ctx:
        yield ctx


@pytest.fixture
def client(app):
    """A test client for the app."""
    return Client(app)