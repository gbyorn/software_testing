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
