import os
from board import create_app
import pytest


@pytest.fixture(scope="module")
def test_app():
    # Set the Testing configuration prior to creating the Flask application
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    yield create_app()


@pytest.fixture(scope="module")
def test_client(test_app):
    # Create a test client using the Flask application configured for testing
    with test_app.test_client() as testing_client:
        # Establish an application context
        with test_app.app_context():
            yield testing_client  # this is where the testing happens!
