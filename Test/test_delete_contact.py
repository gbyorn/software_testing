from Model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(first_name='TestFirstname', middle_name='TestMiddleName',
                                           last_name='TestLastName', nickname='TestNickName', title='TestTitle',
                                           company='TestCompany', address='TestAddress', home_phone='6666666',
                                           mobile_phone='19999999999', work_phone='7777777', fax='123',
                                           first_email='first@mail.ru', second_email='second@mail.ru',
                                           third_email='third@mail.ru', homepage='TestHomepage', b_day='11',
                                           b_month='November', b_year='1991', a_day='11', a_month='November', a_year='2011',
                                           second_address='TestSecAddress', second_home='TestSecHome',
                                           second_notes='TestSecNotes'))
    app.contact.open_addresses_home_page()
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.contact.open_addresses_home_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
