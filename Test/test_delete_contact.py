def test_delete_contact(app):
    app.open_home_page()
    app.session.login(username='admin', password='secret')
    app.contact.open_addresses_home_page()
    app.contact.delete_contact()
    app.contact.open_addresses_home_page()
    app.session.logout()
