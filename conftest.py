import pytest
from Fixture.application import Application


@pytest.fixture()
def app():
    new_app = Application()
    yield new_app
    new_app.webdriver.quit()
