import pytest
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestCreateGroup:
    def setup_method(self):
        self.webdriver = WebDriver()

    def test_create_group(self):
        self.webdriver.get("http://localhost:8080/addressbook/")
        self.webdriver.find_element(By.NAME, "user").click()
        self.webdriver.find_element(By.NAME, "user").clear()
        self.webdriver.find_element(By.NAME, "user").send_keys("admin")
        self.webdriver.find_element(By.NAME, "pass").click()
        self.webdriver.find_element(By.NAME, "pass").clear()
        self.webdriver.find_element(By.NAME, "pass").send_keys("secret")
        self.webdriver.find_element(By.XPATH, "//input[@value='Login']").click()
        self.webdriver.find_element(By.LINK_TEXT, "groups").click()
        self.webdriver.find_element(By.NAME, "new").click()
        self.webdriver.find_element(By.NAME, "group_name").click()
        self.webdriver.find_element(By.NAME, "group_name").send_keys("TestGroup")
        self.webdriver.find_element(By.NAME, "group_header").click()
        self.webdriver.find_element(By.NAME, "group_header").send_keys("TestHeader")
        self.webdriver.find_element(By.NAME, "group_footer").click()
        self.webdriver.find_element(By.NAME, "group_footer").send_keys("TestFooter")
        self.webdriver.find_element(By.NAME, "submit").click()
        self.webdriver.find_element(By.LINK_TEXT, "groups").click()

    def teardown_method(self):
        self.webdriver.quit()
