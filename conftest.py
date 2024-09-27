import pytest

from helper import Helper


@pytest.fixture()
def new_body():
    payload = Helper.generate_create_user()

    yield payload






