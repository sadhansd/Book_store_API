import pytest

@pytest.fixture
def validID():
    return 20

@pytest.fixture
def invalidID():
    return 10000