from Model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create_contact(Contact(first_name='TestFirstname', middle_name='TestMiddleName',
                                           last_name='TestLastName', nickname='TestNickName', title='TestTitle',
                                           company='TestCompany', address='TestAddress', home_phone='6666666',
                                           mobile_phone='19999999999', work_phone='7777777', fax='123',
                                           first_email='first@mail.ru', second_email='second@mail.ru',
                                           third_email='third@mail.ru', homepage='TestHomepage', b_day='11',
                                           b_month='November', b_year='1991', a_day='11', a_month='November',
                                           a_year='2011', second_address='TestSecAddress', second_home='TestSecHome',
                                           second_notes='TestSecNotes'))
    app.contact.open_addresses_home_page()
    old_contacts = db.get_contacts_list()
    index = random.randrange(len(old_contacts))
    contact = Contact(first_name='TestFirstname815', middle_name='TestMiddleName1', last_name='TestLastName1',
                      nickname='TestNickName44', title='TestTitle1', company='TestCompany1', address='TestAddress1',
                      home_phone='66666661', mobile_phone='199999999991', work_phone='77777771', fax='1231',
                      first_email='first@mail.ru1', second_email='second@mail.ru1', third_email='third@mail.ru1',
                      homepage='TestHomepage1', b_day='11', b_month='November', b_year='1991', a_day='11',
                      a_month='November', a_year='2011', second_address='TestSecAddress1', second_home='TestSecHome1',
                      second_notes='TestSecNotes1')
    contact.contact_id = old_contacts[index].contact_id
    app.contact.edit_contact_by_id(contact.contact_id, contact)
    app.contact.open_addresses_home_page()
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
