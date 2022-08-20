import random
from Model.contact import Contact
import time


def test_delete_contact_db(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
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
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.contact_id)
    app.contact.open_addresses_home_page()
    time.sleep(2)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
