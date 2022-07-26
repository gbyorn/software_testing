from Model.contact import Contact


def test_create_contact(app, json_contacts):
    app.contact.open_addresses_home_page()
    old_contacts = app.contact.get_contacts_list()
    contact = json_contacts
    app.contact.create_contact(contact)
    app.contact.open_addresses_home_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
