def test_delete_contact(app):
    app.contact.open_addresses_home_page()
    app.contact.delete_contact()
    app.contact.open_addresses_home_page()
