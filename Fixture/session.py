from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class SessionHelper:

    def __init__(self, app: WebDriver):
        self.app = app

    def login(self, username: str, password: str):
        self.app.find_element(By.NAME, "user").click()
        self.app.find_element(By.NAME, "user").clear()
        self.app.find_element(By.NAME, "user").send_keys(username)
        self.app.find_element(By.NAME, "pass").click()
        self.app.find_element(By.NAME, "pass").clear()
        self.app.find_element(By.NAME, "pass").send_keys(password)
        self.app.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        self.app.find_element(By.LINK_TEXT, "Logout")

    def ensure_login(self, username: str, password: str):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username: str):
        return self.app.find_element(By.XPATH, "//div/div[1]/form/b").text == "(" + username + ")"
