from ..page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def get_tags_locator(tag):
    tags = (By.XPATH, "//span[text()='{}']".format(tag))
    return tags


class PoliticanPage(BasePage):
    url_path = ""

    FULL_NAME = (By.XPATH, "//input[@id='fullName']")
    COUNTRY = (By.XPATH, "//*[@id='country']")
    YOB = (By.XPATH, "//*[@id='root']/div/div/form/div[3]/div/input")
    POSITION = (By.XPATH, "//input[@id='position']")
    URL = (By.XPATH, "//input[@id='url']")
    RISK = (By.XPATH, "//select[@id='risk']")
    SAVE = (By.XPATH, "//button")
    MODAL = (By.XPATH, "//div[@class='modal-body']")
    BACK = (By.XPATH, "//div/button[@class='btn btn-secondary']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_full_name(self, fullname):
        self._type(self.FULL_NAME, fullname)
        return self

    def add_country(self, country):
        self._type(self.COUNTRY, country)
        return self

    def add_yob(self, yob):
        self._type(self.YOB, yob)
        return self

    def add_position(self, position):
        self._type(self.POSITION, position)
        return self

    def add_url(self, url):
        self._type(self.URL, url)
        return self

    def select_risk(self, risk):
        Select(self._find(self.RISK))\
            .select_by_visible_text(risk)
        return self

    def click_save(self):
        save = self._find(self.SAVE)
        save.click()

    def save_record(self):
        self.wait_element_visible(self.MODAL, 10)
        modal = self._find(self.MODAL)
        back = self._find(self.BACK)
        back.click()
        return modal

    # def search_text_on_page(self, text):
        # src = self.driver.page_source
        # return re.search(text, src)

