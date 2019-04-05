from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    base_url = 'http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/'
    url_path = ''

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_url(self, **kwargs):
        url = "/".join([self.base_url, self.url_path])
        url = url.format(kwargs)
        return url

    def open(self, **kwargs) -> 'BasePage':
        self.driver.get(self.get_url(**kwargs))
        return self

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _find_all(self, locator):
        return self.driver.find_elements(*locator)

    def _type(self, locator, text):
        text_area = self._find(locator)
        text_area.clear()
        text_area.send_keys(text)
        return self

    def wait_element_visible(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
