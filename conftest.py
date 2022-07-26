import pytest
import json
import os.path
from Fixture.application import Application


new_app = None
target = None


@pytest.fixture
def app(request):
    global new_app
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as config_file:
            target = json.load(config_file)
    if new_app is None or new_app.is_valid():
        new_app = Application(browser=browser, base_url=target['baseUrl'])
    new_app.open_home_page()
    new_app.session.ensure_login(username=target['username'], password=target['password'])
    return new_app


@pytest.fixture(scope='session', autouse=True)
def teardown(request):
    def finalizer():
        new_app.session.ensure_logout()
        new_app.webdriver.quit()
    request.addfinalizer(finalizer)
    return new_app


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
