import pymysql
from Model.group import Group
from Model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_groups_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                group_list.append(Group(group_id=str(group_id), group_name=name,
                                        group_header=header, group_footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contacts_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (contact_id, first_name, last_name) = row
                contact_list.append(Contact(contact_id=contact_id, first_name=first_name, last_name=last_name))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
