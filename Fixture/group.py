from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from Model.group import Group


class GroupHelper:

    def __init__(self, app: WebDriver):
        self.app = app

    def create(self, group: Group):
        self.app.find_element(By.NAME, "new").click()
        self.app.find_element(By.NAME, "group_name").click()
        self.app.find_element(By.NAME, "group_name").send_keys(group.group_name)
        self.app.find_element(By.NAME, "group_header").click()
        self.app.find_element(By.NAME, "group_header").send_keys(group.group_header)
        self.app.find_element(By.NAME, "group_footer").click()
        self.app.find_element(By.NAME, "group_footer").send_keys(group.group_footer)
        self.app.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        self.app.find_element(By.LINK_TEXT, "groups").click()
