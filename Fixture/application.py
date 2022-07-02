from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Model.group import Group
from Model.contact import Contact
from Fixture.session import SessionHelper
from Fixture.contact import ContactHelper
from Fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.webdriver = WebDriver()
        self.session = SessionHelper(self.webdriver)
        self.group = GroupHelper(self.webdriver)
        self.contact = ContactHelper(self.webdriver)

    def open_home_page(self):
        self.webdriver.get("http://localhost:8080/addressbook/")

    def is_valid(self):
        try:
            current_url = self.webdriver.current_url
            return True
        except:
            return False