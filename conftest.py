import pytest
from utils.helpers import get_drivers

@pytest.fixture
def driver():
    driver = get_drivers()
    yield driver
    driver.quit()


