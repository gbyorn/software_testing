from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from group import Group
from contact import Contact


class Application:

    def __init__(self):
        self.webdriver = WebDriver()
        self.webdriver.implicitly_wait(60)

    def open_home_page(self):
        self.webdriver.get("http://localhost:8080/addressbook/")

    def login(self):
        self.webdriver.find_element(By.NAME, "user").click()
        self.webdriver.find_element(By.NAME, "user").clear()
        self.webdriver.find_element(By.NAME, "user").send_keys("admin")
        self.webdriver.find_element(By.NAME, "pass").click()
        self.webdriver.find_element(By.NAME, "pass").clear()
        self.webdriver.find_element(By.NAME, "pass").send_keys("secret")
        self.webdriver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_groups_page(self):
        self.webdriver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group: Group):
        self.webdriver.find_element(By.NAME, "new").click()
        self.webdriver.find_element(By.NAME, "group_name").click()
        self.webdriver.find_element(By.NAME, "group_name").send_keys(group.group_name)
        self.webdriver.find_element(By.NAME, "group_header").click()
        self.webdriver.find_element(By.NAME, "group_header").send_keys(group.group_header)
        self.webdriver.find_element(By.NAME, "group_footer").click()
        self.webdriver.find_element(By.NAME, "group_footer").send_keys(group.group_footer)
        self.webdriver.find_element(By.NAME, "submit").click()

    def logout(self):
        self.webdriver.find_element(By.LINK_TEXT, "Logout")

    def write_base_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "firstname").click()
        self.webdriver.find_element(By.NAME, "firstname").send_keys(contact.first_name)
        self.webdriver.find_element(By.NAME, "middlename").click()
        self.webdriver.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        self.webdriver.find_element(By.NAME, "lastname").click()
        self.webdriver.find_element(By.NAME, "lastname").send_keys(contact.last_name)
        self.webdriver.find_element(By.NAME, "nickname").click()
        self.webdriver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        file_photo = self.webdriver.find_element(By.XPATH, "//input[@type='file']")
        file_photo.send_keys(contact.photo)
        self.webdriver.find_element(By.NAME, "photo").send_keys(contact.photo)
        self.webdriver.find_element(By.NAME, "title").click()
        self.webdriver.find_element(By.NAME, "title").send_keys(contact.title)
        self.webdriver.find_element(By.NAME, "company").click()
        self.webdriver.find_element(By.NAME, "company").send_keys(contact.company)
        self.webdriver.find_element(By.NAME, "address").click()
        self.webdriver.find_element(By.NAME, "address").send_keys(contact.address)

    def write_phone_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "home").click()
        self.webdriver.find_element(By.NAME, "home").send_keys(contact.home_phone)
        self.webdriver.find_element(By.NAME, "mobile").click()
        self.webdriver.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        self.webdriver.find_element(By.NAME, "work").click()
        self.webdriver.find_element(By.NAME, "work").send_keys(contact.work_phone)
        self.webdriver.find_element(By.NAME, "fax").click()
        self.webdriver.find_element(By.NAME, "fax").send_keys(contact.fax)

    def write_email_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "email").click()
        self.webdriver.find_element(By.NAME, "email").send_keys(contact.first_email)
        self.webdriver.find_element(By.NAME, "email2").click()
        self.webdriver.find_element(By.NAME, "email2").send_keys(contact.second_email)
        self.webdriver.find_element(By.NAME, "email3").click()
        self.webdriver.find_element(By.NAME, "email3").send_keys(contact.third_email)

    def select_birthday(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "bday").click()
        dropdown = self.webdriver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.b_day}']").click()
        self.webdriver.find_element(By.NAME, "bmonth").click()
        dropdown = self.webdriver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.b_month}']").click()
        self.webdriver.find_element(By.NAME, "byear").click()
        self.webdriver.find_element(By.NAME, "byear").send_keys(contact.b_year)

    def select_anniversary(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "aday").click()
        dropdown = self.webdriver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.a_day}']").click()
        self.webdriver.find_element(By.NAME, "amonth").click()
        dropdown = self.webdriver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.a_month}']").click()
        self.webdriver.find_element(By.NAME, "ayear").click()
        self.webdriver.find_element(By.NAME, "ayear").send_keys(contact.a_year)

    def write_secondary_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "address2").click()
        self.webdriver.find_element(By.NAME, "address2").send_keys(contact.second_address)
        self.webdriver.find_element(By.NAME, "phone2").click()
        self.webdriver.find_element(By.NAME, "phone2").send_keys(contact.second_home)
        self.webdriver.find_element(By.NAME, "notes").click()
        self.webdriver.find_element(By.NAME, "notes").send_keys(contact.second_notes)

    def write_additional_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "homepage").click()
        self.webdriver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        self.select_birthday(contact)
        self.select_anniversary(contact)

    def create_contact(self, contact: Contact):
        self.webdriver.find_element(By.LINK_TEXT, "add new").click()
        self.write_base_info(contact)
        self.write_phone_info(contact)
        self.write_email_info(contact)
        self.write_additional_info(contact)
        self.write_secondary_info(contact)
        self.webdriver.find_element(By.NAME, "submit").click()

    def open_addresses_home_page(self):
        self.webdriver.find_element(By.LINK_TEXT, "home").click()
