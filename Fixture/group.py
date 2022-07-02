from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from Model.group import Group


class GroupHelper:

    def __init__(self, app: WebDriver):
        self.app = app

    def write_data(self, group: Group):
        self.app.find_element(By.NAME, "group_name").click()
        self.app.find_element(By.NAME, "group_name").clear()
        self.app.find_element(By.NAME, "group_name").send_keys(group.group_name)
        self.app.find_element(By.NAME, "group_header").click()
        self.app.find_element(By.NAME, "group_header").clear()
        self.app.find_element(By.NAME, "group_header").send_keys(group.group_name)
        self.app.find_element(By.NAME, "group_footer").click()
        self.app.find_element(By.NAME, "group_footer").clear()
        self.app.find_element(By.NAME, "group_footer").send_keys(group.group_name)

    def create(self, group: Group):
        self.app.find_element(By.NAME, "new").click()
        self.write_data(group)
        self.app.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        self.app.find_element(By.LINK_TEXT, "groups").click()

    def edit(self, group: Group):
        self.app.find_element(By.NAME, "selected[]").click()
        self.app.find_element(By.NAME, "edit").click()
        self.write_data(group)
        self.app.find_element(By.NAME, "update").click()

    def delete(self):
        self.app.find_element(By.NAME, "selected[]").click()
        self.app.find_element(By.NAME, "delete").click()

    def count(self):
        self.open_groups_page()
        return len(self.app.find_elements(By.NAME, "selected[]"))