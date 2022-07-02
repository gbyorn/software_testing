import pytest
from Fixture.application import Application


new_app = None


@pytest.fixture()
def app():
    global new_app
    if new_app is None:
        new_app = Application()
        new_app.open_home_page()
        new_app.session.ensure_login(username='admin', password='secret')
    else:
        if not new_app.is_valid():
            fixture = Application()
            new_app.open_home_page()
            fixture.session.ensure_login(username='admin', password='secret')

    yield new_app
    new_app.session.ensure_logout()
    new_app.webdriver.quit()
