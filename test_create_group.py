from application import Application
from group import Group
import pytest


@pytest.fixture()
def app():
    new_app = Application()
    yield new_app
    new_app.webdriver.quit()


def test_create_group(app):
    app.open_home_page()
    app.login()
    app.open_groups_page()
    app.create_group(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.open_groups_page()
