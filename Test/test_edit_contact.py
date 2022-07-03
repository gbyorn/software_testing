from Model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
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
    app.contact.edit_contact(Contact(first_name='TestFirstname1', middle_name='TestMiddleName1',
                                     last_name='TestLastName1', nickname='TestNickName1', title='TestTitle1',
                                     company='TestCompany1', address='TestAddress1', home_phone='66666661',
                                     mobile_phone='199999999991', work_phone='77777771', fax='1231',
                                     first_email='first@mail.ru1', second_email='second@mail.ru1',
                                     third_email='third@mail.ru1', homepage='TestHomepage1', b_day='11',
                                     b_month='November', b_year='1991', a_day='11', a_month='November', a_year='2011',
                                     second_address='TestSecAddress1', second_home='TestSecHome1',
                                     second_notes='TestSecNotes1'))
    app.contact.open_addresses_home_page()
