import re
from Model.contact import Contact


def test_compare_contacts(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name.strip()
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name.strip()
    assert contact_from_home_page.address == contact_from_edit_page.address.strip()
    assert contact_from_home_page.all_emails_from_home_page == merge_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)


def clear(data: str) -> str:
    return re.sub("[() -]", "", data)


def merge_phones(contact: Contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.second_home]))))


def merge_emails(contact: Contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: x.strip(),
                                filter(lambda x: x is not None,
                                       [contact.first_email, contact.second_email, contact.third_email]))))
