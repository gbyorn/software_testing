from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from Model.group import Group


class GroupHelper:

    def __init__(self, app: WebDriver):
        self.app = app
        self.group_cache = None

    def write_data(self, group: Group):
        self.app.find_element(By.NAME, "group_name").click()
        self.app.find_element(By.NAME, "group_name").clear()
        self.app.find_element(By.NAME, "group_name").send_keys(group.group_name)
        self.app.find_element(By.NAME, "group_header").click()
        self.app.find_element(By.NAME, "group_header").clear()
        self.app.find_element(By.NAME, "group_header").send_keys(group.group_header)
        self.app.find_element(By.NAME, "group_footer").click()
        self.app.find_element(By.NAME, "group_footer").clear()
        self.app.find_element(By.NAME, "group_footer").send_keys(group.group_footer)

    def create_group(self, group: Group):
        self.app.find_element(By.NAME, "new").click()
        self.write_data(group)
        self.app.find_element(By.NAME, "submit").click()
        self.group_cache = None

    def open_groups_page(self):
        if not (self.app.current_url.endswith("/group.php")
                and len(self.app.find_elements(By.XPATH, "//input[@value='New group']")) > 0):
            self.app.find_element(By.LINK_TEXT, "groups").click()

    def edit_group_by_index(self, index, group: Group):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.app.find_element(By.NAME, "edit").click()
        self.write_data(group)
        self.app.find_element(By.NAME, "update").click()
        self.group_cache = None

    def edit_group_by_id(self, group_id, group: Group):
        self.open_groups_page()
        self.select_group_by_id(group_id)
        self.app.find_element(By.NAME, "edit").click()
        self.write_data(group)
        self.app.find_element(By.NAME, "update").click()
        self.group_cache = None

    def edit_first_group(self, group: Group):
        self.edit_group_by_index(0, group)

    def select_group_by_index(self, index):
        self.open_groups_page()
        self.app.find_elements(By.NAME, 'selected[]')[index].click()

    def select_group_by_id(self, group_id):
        self.open_groups_page()
        self.app.find_element(By.CSS_SELECTOR, f"input[value='{group_id}'").click()

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.app.find_element(By.NAME, "delete").click()
        self.group_cache = None

    def delete_group_by_id(self, group_id):
        self.open_groups_page()
        self.select_group_by_id(group_id)
        self.app.find_element(By.NAME, "delete").click()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def count_groups(self):
        self.open_groups_page()
        return len(self.app.find_elements(By.NAME, "selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in self.app.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                group_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, group_id=group_id))
        return list(self.group_cache)

