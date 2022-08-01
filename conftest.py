import jsonpickle
import pytest
import json
import os.path
import importlib
from Fixture.application import Application
from Fixture.db import DbFixture


new_app = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as conf_file:
            target = json.load(conf_file)
    return target


@pytest.fixture
def app(request):
    global new_app
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if new_app is None or not new_app.is_valid():
        new_app = Application(browser=browser, base_url=web_config['baseUrl'])
    new_app.open_home_page()
    new_app.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return new_app


@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope='session', autouse=True)
def teardown(request):
    def finalizer():
        new_app.session.ensure_logout()
        new_app.webdriver.quit()
    request.addfinalizer(finalizer)
    return new_app


@pytest.fixture()
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module(f"data.{module}").testdata


def load_from_json(json_file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{json_file}.json")) as json_file:
        return jsonpickle.decode(json_file.read())
