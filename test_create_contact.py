from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestCreateContact:
    def setup_method(self):
        self.webdriver = WebDriver()

    def test_create_contact(self):
        self.open_home_page()
        self.login()
        self.create_contact()
        self.open_addresses_home_page()
        self.logout()

    def create_contact(self):
        self.webdriver.find_element(By.LINK_TEXT, "add new").click()
        self.write_base_info()
        self.write_phone_info()
        self.write_email_info()
        self.write_additional_info()
        self.write_secondary_info()
        self.webdriver.find_element(By.NAME, "submit").click()

    def write_additional_info(self):
        self.webdriver.find_element(By.NAME, "homepage").click()
        self.webdriver.find_element(By.NAME, "homepage").send_keys("Test homepage")
        self.select_birthday()
        self.select_anniversary()

    def write_secondary_info(self):
        self.webdriver.find_element(By.NAME, "address2").click()
        self.webdriver.find_element(By.NAME, "address2").send_keys("Test secondary address")
        self.webdriver.find_element(By.NAME, "phone2").click()
        self.webdriver.find_element(By.NAME, "phone2").send_keys("Test secondary home phone")
        self.webdriver.find_element(By.NAME, "notes").click()
        self.webdriver.find_element(By.NAME, "notes").send_keys("Test some notes")

    def select_anniversary(self):
        self.webdriver.find_element(By.NAME, "aday").click()
        dropdown = self.webdriver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = '10']").click()
        self.webdriver.find_element(By.NAME, "amonth").click()
        dropdown = self.webdriver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = 'October']").click()
        self.webdriver.find_element(By.NAME, "ayear").click()
        self.webdriver.find_element(By.NAME, "ayear").send_keys("2010")

    def select_birthday(self):
        self.webdriver.find_element(By.NAME, "bday").click()
        dropdown = self.webdriver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '10']").click()
        self.webdriver.find_element(By.NAME, "bmonth").click()
        dropdown = self.webdriver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = 'October']").click()
        self.webdriver.find_element(By.NAME, "byear").click()
        self.webdriver.find_element(By.NAME, "byear").send_keys("1990")

    def write_email_info(self):
        self.webdriver.find_element(By.NAME, "email").click()
        self.webdriver.find_element(By.NAME, "email").send_keys("Test first email")
        self.webdriver.find_element(By.NAME, "email2").click()
        self.webdriver.find_element(By.NAME, "email2").send_keys("Test second email")
        self.webdriver.find_element(By.NAME, "email3").click()
        self.webdriver.find_element(By.NAME, "email3").send_keys("Test third email")

    def write_phone_info(self):
        self.webdriver.find_element(By.NAME, "home").click()
        self.webdriver.find_element(By.NAME, "home").send_keys("Test home telephone")
        self.webdriver.find_element(By.NAME, "mobile").click()
        self.webdriver.find_element(By.NAME, "mobile").send_keys("Test mobile telephone")
        self.webdriver.find_element(By.NAME, "work").click()
        self.webdriver.find_element(By.NAME, "work").send_keys("Test work telephone")
        self.webdriver.find_element(By.NAME, "fax").click()
        self.webdriver.find_element(By.NAME, "fax").send_keys("Test fax")

    def write_base_info(self):
        self.webdriver.find_element(By.NAME, "firstname").click()
        self.webdriver.find_element(By.NAME, "firstname").send_keys("TestFirstName")
        self.webdriver.find_element(By.NAME, "middlename").click()
        self.webdriver.find_element(By.NAME, "middlename").send_keys("TestMiddleName")
        self.webdriver.find_element(By.NAME, "lastname").click()
        self.webdriver.find_element(By.NAME, "lastname").send_keys("TestLastName")
        self.webdriver.find_element(By.NAME, "nickname").click()
        self.webdriver.find_element(By.NAME, "nickname").send_keys("TestNickname")
        self.webdriver.find_element(By.NAME, "title").click()
        self.webdriver.find_element(By.NAME, "title").send_keys("TestTitle")
        self.webdriver.find_element(By.NAME, "company").click()
        self.webdriver.find_element(By.NAME, "company").send_keys("TestCompany")
        self.webdriver.find_element(By.NAME, "address").click()
        self.webdriver.find_element(By.NAME, "address").send_keys("Test some address")

    def open_addresses_home_page(self):
        self.webdriver.find_element(By.LINK_TEXT, "home page").click()

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
