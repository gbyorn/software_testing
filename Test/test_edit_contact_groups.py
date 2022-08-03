from Model.contact import Contact
from Model.group import Group
from Fixture.orm import ORMFixture
import random


database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_group_to_contact(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.create_group(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))

    groups = db.get_groups_list()
    group = random.choice(groups)
    contacts_in_groups_before = database.get_contacts_in_group(group)

    contacts = [contact for contact in database.get_contacts_not_in_group(group)
                if contact not in contacts_in_groups_before]

    if len(db.get_contacts_list()) == 0 or len(contacts) == 0:
        new_contact = Contact(first_name='UserForGroup')
        app.contact.create_contact(new_contact)
        contacts.append(new_contact)

    contact = random.choice(contacts)

    app.contact.add_contact_to_group(group_name=group.group_name, contact_id=contact.contact_id)
    contacts_in_groups_after = database.get_contacts_in_group(group)

    assert contact in contacts_in_groups_after
    assert len(contacts_in_groups_before) + 1 == len(contacts_in_groups_after)


def test_remove_group_to_contact(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.create_group(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))

    groups = db.get_groups_list()
    group = random.choice(groups)
    contacts_in_groups_before = database.get_contacts_in_group(group)

    if len(db.get_contacts_list()) == 0 or len(contacts_in_groups_before) == 0:
        app.contact.create_contact(Contact(first_name='TestFirstname', group_name=group.group_name))
        contacts_in_groups_before = database.get_contacts_in_group(group)

    contacts = [contact for contact in database.get_contacts_in_group(group)
                if contact in contacts_in_groups_before]

    contact = random.choice(contacts)

    app.contact.remove_contact_from_group(group_name=group.group_name, contact_id=contact.contact_id)
    contacts_in_groups_after = database.get_contacts_in_group(group)

    assert contact not in contacts_in_groups_after
    assert len(contacts_in_groups_before) - 1 == len(contacts_in_groups_after)
