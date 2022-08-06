from pony.orm import *
from datetime import datetime
from Model.group import Group
from Model.contact import Contact
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        group_id = PrimaryKey(int, column='group_id')
        group_name = Optional(str, column='group_name')
        group_header = Optional(str, column='group_header')
        group_footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id",
                       reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        contact_id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        second_home = Optional(str, column='phone2')
        first_email = Optional(str, column='email')
        second_email = Optional(str, column='email2')
        third_email = Optional(str, column='email3')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id",
                     reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group: Group):
            return Group(group_id=str(group.group_id), group_name=group.group_name,
                         group_header=group.group_header, group_footer=group.group_footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(group for group in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact: Contact):
            return Contact(contact_id=str(contact.contact_id), first_name=contact.first_name.strip(),
                           last_name=contact.last_name.strip(), address=contact.address.strip(),
                           home_phone=contact.home_phone, work_phone=contact.work_phone,
                           mobile_phone=contact.mobile_phone, second_home=contact.second_home,
                           first_email=contact.first_email, second_email=contact.second_email,
                           third_email=contact.third_email)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(contact for contact in ORMFixture.ORMContact
                                                     if contact.deprecated is None))

    @db_session
    def get_contacts_in_group(self, target_group: Group):
        orm_group = list(select(group for group in ORMFixture.ORMGroup if group.group_id == target_group.group_id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, target_group: Group):
        orm_group = list(select(group for group in ORMFixture.ORMGroup if group.group_id == target_group.group_id))[0]
        return self.convert_contacts_to_model(
            select(contact for contact in ORMFixture.ORMContact if contact.deprecated is None
                   and orm_group not in contact.groups))
