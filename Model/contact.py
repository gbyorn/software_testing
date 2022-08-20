from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None,
                 company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 first_email=None, second_email=None, third_email=None, homepage=None, b_day=None, b_month=None,
                 b_year=None, a_day=None, a_month=None, a_year=None, second_address=None, second_home=None,
                 second_notes=None, contact_id=None, all_phones_from_home_page=None, all_emails_from_home_page=None,
                 group_name=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.first_email = first_email
        self.second_email = second_email
        self.third_email = third_email
        self.homepage = homepage
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.a_day = a_day
        self. a_month = a_month
        self.a_year = a_year
        self.second_address = second_address
        self.second_home = second_home
        self.second_notes = second_notes
        self.contact_id = contact_id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.group_name = group_name

    def __repr__(self):
        return f'{self.contact_id}: {self.first_name} -- {self.last_name}'

    def __eq__(self, other):
        return (self.contact_id == other.contact_id or self.contact_id is None or other.contact_id is None) \
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        return int(self.contact_id) if self.contact_id else maxsize
