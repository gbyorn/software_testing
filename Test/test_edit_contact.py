from Model.contact import Contact


def test_edit_contact(app):
    app.open_home_page()
    app.session.login(username='admin', password='secret')
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
    app.session.logout()
