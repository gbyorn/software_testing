from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from Model.contact import Contact


class ContactHelper:

    def __init__(self, app: WebDriver):
        self.app = app

    def write_base_info(self, contact: Contact):
        self.app.find_element(By.NAME, "firstname").click()
        self.app.find_element(By.NAME, "firstname").clear()
        self.app.find_element(By.NAME, "firstname").send_keys(contact.first_name)
        self.app.find_element(By.NAME, "middlename").click()
        self.app.find_element(By.NAME, "middlename").clear()
        self.app.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        self.app.find_element(By.NAME, "lastname").click()
        self.app.find_element(By.NAME, "lastname").clear()
        self.app.find_element(By.NAME, "lastname").send_keys(contact.last_name)
        self.app.find_element(By.NAME, "nickname").click()
        self.app.find_element(By.NAME, "nickname").clear()
        self.app.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        file_photo = self.app.find_element(By.XPATH, "//input[@type='file']")
        file_photo.send_keys(contact.photo)
        self.app.find_element(By.NAME, "photo").send_keys(contact.photo)
        self.app.find_element(By.NAME, "title").click()
        self.app.find_element(By.NAME, "title").clear()
        self.app.find_element(By.NAME, "title").send_keys(contact.title)
        self.app.find_element(By.NAME, "company").click()
        self.app.find_element(By.NAME, "company").clear()
        self.app.find_element(By.NAME, "company").send_keys(contact.company)
        self.app.find_element(By.NAME, "address").click()
        self.app.find_element(By.NAME, "address").clear()
        self.app.find_element(By.NAME, "address").send_keys(contact.address)

    def write_phone_info(self, contact: Contact):
        self.app.find_element(By.NAME, "home").click()
        self.app.find_element(By.NAME, "home").clear()
        self.app.find_element(By.NAME, "home").send_keys(contact.home_phone)
        self.app.find_element(By.NAME, "mobile").click()
        self.app.find_element(By.NAME, "mobile").clear()
        self.app.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        self.app.find_element(By.NAME, "work").click()
        self.app.find_element(By.NAME, "work").clear()
        self.app.find_element(By.NAME, "work").send_keys(contact.work_phone)
        self.app.find_element(By.NAME, "fax").click()
        self.app.find_element(By.NAME, "fax").clear()
        self.app.find_element(By.NAME, "fax").send_keys(contact.fax)

    def write_email_info(self, contact: Contact):
        self.app.find_element(By.NAME, "email").click()
        self.app.find_element(By.NAME, "email").clear()
        self.app.find_element(By.NAME, "email").send_keys(contact.first_email)
        self.app.find_element(By.NAME, "email2").click()
        self.app.find_element(By.NAME, "email2").clear()
        self.app.find_element(By.NAME, "email2").send_keys(contact.second_email)
        self.app.find_element(By.NAME, "email3").click()
        self.app.find_element(By.NAME, "email3").clear()
        self.app.find_element(By.NAME, "email3").send_keys(contact.third_email)

    def select_birthday(self, contact: Contact):
        self.app.find_element(By.NAME, "bday").click()
        dropdown = self.app.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.b_day}']").click()
        self.app.find_element(By.NAME, "bmonth").click()
        dropdown = self.app.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.b_month}']").click()
        self.app.find_element(By.NAME, "byear").click()
        self.app.find_element(By.NAME, "byear").send_keys(contact.b_year)

    def select_anniversary(self, contact: Contact):
        self.app.find_element(By.NAME, "aday").click()
        dropdown = self.app.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.a_day}']").click()
        self.app.find_element(By.NAME, "amonth").click()
        dropdown = self.app.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.a_month}']").click()
        self.app.find_element(By.NAME, "ayear").click()
        self.app.find_element(By.NAME, "ayear").send_keys(contact.a_year)

    def write_secondary_info(self, contact: Contact):
        self.app.find_element(By.NAME, "address2").click()
        self.app.find_element(By.NAME, "address2").clear()
        self.app.find_element(By.NAME, "address2").send_keys(contact.second_address)
        self.app.find_element(By.NAME, "phone2").click()
        self.app.find_element(By.NAME, "phone2").clear()
        self.app.find_element(By.NAME, "phone2").send_keys(contact.second_home)
        self.app.find_element(By.NAME, "notes").click()
        self.app.find_element(By.NAME, "notes").clear()
        self.app.find_element(By.NAME, "notes").send_keys(contact.second_notes)

    def write_additional_info(self, contact: Contact):
        self.app.find_element(By.NAME, "homepage").click()
        self.app.find_element(By.NAME, "homepage").clear()
        self.app.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        self.select_birthday(contact)
        self.select_anniversary(contact)

    def create_contact(self, contact: Contact):
        self.app.find_element(By.LINK_TEXT, "add new").click()
        self.write_base_info(contact)
        self.write_phone_info(contact)
        self.write_email_info(contact)
        self.write_additional_info(contact)
        self.write_secondary_info(contact)
        self.app.find_element(By.NAME, "submit").click()

    def open_addresses_home_page(self):
        self.app.find_element(By.LINK_TEXT, "home").click()

    def edit_contact(self, contact: Contact):
        self.app.find_element(By.NAME, "selected[]").click()
        self.app.find_element(By.XPATH, '//*[@title="Edit"]').click()
        self.write_base_info(contact)
        self.write_phone_info(contact)
        self.write_email_info(contact)
        self.write_additional_info(contact)
        self.write_secondary_info(contact)
        self.app.find_element(By.NAME, "update").click()

    def delete_contact(self):
        self.app.find_element(By.NAME, "selected[]").click()
        self.app.find_element(By.XPATH, '//*[@value="Delete"]').click()
        self.app.switch_to.alert.accept()
