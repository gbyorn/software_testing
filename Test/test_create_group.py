from Fixture.application import Application
from Model.group import Group
import pytest


@pytest.fixture()
def app():
    new_app = Application()
    yield new_app
    new_app.webdriver.quit()


def test_create_group(app):
    app.open_home_page()
    app.session.login(username='admin', password='secret')
    app.group.open_groups_page()
    app.group.create(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    app.session.logout()
