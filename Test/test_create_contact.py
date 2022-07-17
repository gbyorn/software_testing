from Model.contact import Contact
import pytest
import random
import string


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + (" " * 10)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Contact(first_name=random_string("firstname", 10), middle_name=random_string("middlename", 10),
                     last_name=random_string("lastname", 10), nickname=random_string("nickname", 10),
                     title=random_string("title", 15), company=random_string("title", 15),
                     address=random_string("title", 20), home_phone=random_string("h", 5),
                     mobile_phone=random_string("m", 5), work_phone=random_string("w", 5),
                     fax=random_string("fax", 5), first_email=random_string("first", 5),
                     second_email=random_string("second", 5), third_email=random_string("third", 5),
                     homepage=random_string("homepage", 10), b_day=str(random.randint(1, 31)),
                     b_month=random.choice(['October', 'April', 'May']), b_year=str(random.randint(1980, 2010)),
                     a_day=str(random.randint(1, 31)), a_month=random.choice(['November', 'June', 'July']),
                     a_year=str(random.randint(1980, 2010)), second_address=random_string("secondaddr", 10),
                     second_home=random_string("s", 5), second_notes=random_string("secondnote", 10))
             for i in range(1)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_create_contact(app, contact):
    app.contact.open_addresses_home_page()
    old_contacts = app.contact.get_contacts_list()
    contact = contact
    app.contact.create_contact(contact)
    app.contact.open_addresses_home_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
