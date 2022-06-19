from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from contact import Contact


class TestCreateContact:
    def setup_method(self):
        self.webdriver = WebDriver()
        self.new_contact = Contact(first_name='TestFirstname', middle_name='TestMiddleName', last_name='TestLastName',
                                   nickname='TestNickName', title='TestTitle', company='TestCompany',
                                   address='TestAddress', home_phone='6666666', mobile_phone='19999999999',
                                   work_phone='7777777', fax='123', first_email='first@mail.ru',
                                   second_email='second@mail.ru', third_email='third@mail.ru', homepage='TestHomepage',
                                   b_day='10', b_month='October', b_year='1990',
                                   a_day='10', a_month='October', a_year='2010',
                                   second_address='TestSecAddress', second_home='TestSecHome',
                                   second_notes='TestSecNotes', photo='C:\\photo.png')

    def test_create_contact(self):
        self.open_home_page()
        self.login()
        self.create_contact(self.new_contact)
        self.open_addresses_home_page()
        self.logout()

    def create_contact(self, contact: Contact):
        self.webdriver.find_element(By.LINK_TEXT, "add new").click()
        self.write_base_info(contact)
        self.write_phone_info(contact)
        self.write_email_info(contact)
        self.write_additional_info(contact)
        self.write_secondary_info(contact)
        self.webdriver.find_element(By.NAME, "submit").click()

    def write_additional_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "homepage").click()
        self.webdriver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        self.select_birthday(contact)
        self.select_anniversary(contact)

    def write_secondary_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "address2").click()
        self.webdriver.find_element(By.NAME, "address2").send_keys(contact.second_address)
        self.webdriver.find_element(By.NAME, "phone2").click()
        self.webdriver.find_element(By.NAME, "phone2").send_keys(contact.second_home)
        self.webdriver.find_element(By.NAME, "notes").click()
        self.webdriver.find_element(By.NAME, "notes").send_keys(contact.second_notes)

    def select_anniversary(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "aday").click()
        dropdown = self.webdriver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.a_day}']").click()
        self.webdriver.find_element(By.NAME, "amonth").click()
        dropdown = self.webdriver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.a_month}']").click()
        self.webdriver.find_element(By.NAME, "ayear").click()
        self.webdriver.find_element(By.NAME, "ayear").send_keys(contact.a_year)

    def select_birthday(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "bday").click()
        dropdown = self.webdriver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.b_day}']").click()
        self.webdriver.find_element(By.NAME, "bmonth").click()
        dropdown = self.webdriver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.b_month}']").click()
        self.webdriver.find_element(By.NAME, "byear").click()
        self.webdriver.find_element(By.NAME, "byear").send_keys(contact.b_year)

    def write_email_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "email").click()
        self.webdriver.find_element(By.NAME, "email").send_keys(contact.first_email)
        self.webdriver.find_element(By.NAME, "email2").click()
        self.webdriver.find_element(By.NAME, "email2").send_keys(contact.second_email)
        self.webdriver.find_element(By.NAME, "email3").click()
        self.webdriver.find_element(By.NAME, "email3").send_keys(contact.third_email)

    def write_phone_info(self, contact: Contact):
        self.webdriver.find_element(By.NAME, "home").click()
        self.webdriver.find_element(By.NAME, "home").send_keys(contact.home_phone)
        self.webdriver.find_element(By.NAME, "mobile").click()
        self.webdriver.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        self.webdriver.find_element(By.NAME, "work").click()
        self.webdriver.find_element(By.NAME, "work").send_keys(contact.work_phone)
        self.webdriver.find_element(By.NAME, "fax").click()
        self.webdriver.find_element(By.NAME, "fax").send_keys(contact.fax)

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

    def open_addresses_home_page(self):
        self.webdriver.find_element(By.LINK_TEXT, "home").click()

    def logout(self):
        self.webdriver.find_element(By.LINK_TEXT, "Logout").click()

    def login(self):
        self.webdriver.find_element(By.NAME, "user").click()
        self.webdriver.find_element(By.NAME, "user").clear()
        self.webdriver.find_element(By.NAME, "user").send_keys("admin")
        self.webdriver.find_element(By.NAME, "pass").click()
        self.webdriver.find_element(By.NAME, "pass").clear()
        self.webdriver.find_element(By.NAME, "pass").send_keys("secret")
        self.webdriver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self):
        self.webdriver.get("http://localhost:8080/addressbook/")

    def teardown_method(self):
        self.webdriver.quit()
