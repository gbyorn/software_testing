from Fixture.application import Application
from Model.contact import Contact
import pytest


@pytest.fixture()
def app():
    new_app = Application()
    yield new_app
    new_app.webdriver.quit()


def test_create_contact(app):
    app.open_home_page()
    app.session.login(username='admin', password='secret')
    app.contact.create_contact(Contact(first_name='TestFirstname', middle_name='TestMiddleName',
                                       last_name='TestLastName', nickname='TestNickName', title='TestTitle',
                                       company='TestCompany', address='TestAddress', home_phone='6666666',
                                       mobile_phone='19999999999', work_phone='7777777', fax='123',
                                       first_email='first@mail.ru', second_email='second@mail.ru',
                                       third_email='third@mail.ru', homepage='TestHomepage', b_day='10',
                                       b_month='October', b_year='1990', a_day='10', a_month='October', a_year='2010',
                                       second_address='TestSecAddress', second_home='TestSecHome',
                                       second_notes='TestSecNotes', photo='C:\\photo.png'))
    app.contact.open_addresses_home_page()
    app.session.logout()
