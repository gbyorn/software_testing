import pytest
from Fixture.application import Application


new_app = None


@pytest.fixture()
def app(request):
    global new_app
    if new_app is None:
        new_app = Application()
    else:
        if not new_app.is_valid():
            new_app = Application()
    new_app.open_home_page()
    new_app.session.ensure_login(username='admin', password='secret')
    return new_app


@pytest.fixture(scope='session', autouse=True)
def teardown(request):
    def finalizer():
        new_app.session.ensure_logout()
        new_app.webdriver.quit()
    request.addfinalizer(finalizer)
    return new_app
