from Model.contact import Contact
from Model.group import Group
from Fixture.orm import ORMFixture
import random


database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_group_to_contact(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.open_groups_page()
        app.group.create_group(Group(group_name='GroupForUser', group_header='', group_footer=''))

    groups = db.get_groups_list()
    group = random.choice(groups)
    contacts_in_groups_before = database.get_contacts_in_group(group)

    contacts = [contact for contact in database.get_contacts_not_in_group(group)
                if contact not in contacts_in_groups_before]

    if len(db.get_contacts_list()) == 0 or len(contacts) == 0:
        app.contact.open_addresses_home_page()
        app.contact.create_contact(Contact(first_name='Contact_without_group', middle_name='', last_name='', nickname='',
                                           title='', company='', address='', home_phone='', mobile_phone='',
                                           work_phone='', fax='', first_email='', second_email='', third_email='',
                                           homepage='', b_day='-', b_month='-', b_year='', a_day='-', a_month='-',
                                           a_year='', second_address='', second_home='', second_notes=''))
        contacts = database.get_contacts_not_in_group(group)

    contact = random.choice(contacts)

    app.contact.add_contact_to_group(group_name=group.group_name, contact_id=contact.contact_id)
    contacts_in_groups_after = database.get_contacts_in_group(group)

    assert contact in contacts_in_groups_after
    assert len(contacts_in_groups_before) + 1 == len(contacts_in_groups_after)


def test_remove_group_to_contact(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.open_groups_page()
        app.group.create_group(Group(group_name='GroupForUser', group_header='', group_footer=''))

    groups = db.get_groups_list()
    group = random.choice(groups)
    contacts_in_groups_before = database.get_contacts_in_group(group)

    if len(db.get_contacts_list()) == 0 or len(contacts_in_groups_before) == 0:
        app.contact.open_addresses_home_page()
        app.contact.create_contact(Contact(first_name='Contact_with_group', middle_name='', last_name='', nickname='',
                                           title='', company='', address='', home_phone='', mobile_phone='',
                                           work_phone='', fax='', first_email='', second_email='', third_email='',
                                           homepage='', b_day='-', b_month='-', b_year='', a_day='-', a_month='-',
                                           a_year='', second_address='', second_home='', second_notes='',
                                           group_name=group.group_name))
        contacts_in_groups_before = database.get_contacts_in_group(group)

    contacts = [contact for contact in database.get_contacts_in_group(group)
                if contact in contacts_in_groups_before]

    contact = random.choice(contacts)

    app.contact.remove_contact_from_group(group_name=group.group_name, contact_id=contact.contact_id)
    contacts_in_groups_after = database.get_contacts_in_group(group)

    assert contact not in contacts_in_groups_after
    assert len(contacts_in_groups_before) - 1 == len(contacts_in_groups_after)
