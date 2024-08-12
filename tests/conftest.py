import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def app():
    app = create_app()
    # setup
    yield app
    # teardown

@pytest.fixture
def client(app):
    return app.test_client()    # simulates requests