from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from group import Group


class TestCreateGroup:
    def setup_method(self):
        self.webdriver = WebDriver()
        self.new_group = Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter')

    def test_create_group(self):
        self.open_home_page()
        self.login()
        self.open_groups_page()
        self.create_group(self.new_group)
        self.open_groups_page()
        self.logout()

    def logout(self):
        self.webdriver.find_element(By.LINK_TEXT, "Logout")

    def create_group(self, group: Group):
        self.webdriver.find_element(By.NAME, "new").click()
        self.webdriver.find_element(By.NAME, "group_name").click()
        self.webdriver.find_element(By.NAME, "group_name").send_keys(group.group_name)
        self.webdriver.find_element(By.NAME, "group_header").click()
        self.webdriver.find_element(By.NAME, "group_header").send_keys(group.group_header)
        self.webdriver.find_element(By.NAME, "group_footer").click()
        self.webdriver.find_element(By.NAME, "group_footer").send_keys(group.group_footer)
        self.webdriver.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        self.webdriver.find_element(By.LINK_TEXT, "groups").click()

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
