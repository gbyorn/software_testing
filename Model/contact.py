from sys import maxsize


class Contact:
    def __init__(self, first_name: str | None = None, middle_name: str | None = None, last_name: str | None = None,
                 nickname: str | None = None, title: str | None = None, company: str | None = None,
                 address: str | None = None, home_phone: str | None = None, mobile_phone: str | None = None,
                 work_phone: str | None = None, fax: str | None = None, first_email: str | None = None,
                 second_email: str | None = None, third_email: str | None = None, homepage: str | None = None,
                 b_day: str | None = None, b_month: str | None = None, b_year: str | None = None,
                 a_day: str | None = None, a_month: str | None = None, a_year: str | None = None,
                 second_address: str | None = None, second_home: str | None = None, second_notes: str | None = None,
                 contact_id: str | None = None, all_phones_from_home_page=None, all_emails_from_home_page=None,
                 group_name: str | None = None):
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
