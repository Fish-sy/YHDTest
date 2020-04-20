# coding = utf-8
from selenium import webdriver


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def _open(self, url):
        self.driver.get(url)

    def open(self, base_url):
        self._open(base_url)

    def by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            print(f"页面未定位到 {xpath} 元素!")

    def click(self, webelement):
        webelement.click()

    def send_key(self, webelement, keys):
        webelement.clear()
        webelement.send_keys(keys)

    def quit(self):
        self.driver.quit()

    def submit(self, xpath):
        element = self.by_xpath(xpath)
        element.submit()

    def handle(self, value):
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[value])
        except:
            print(f"根据 {value} 获取句柄失败!")

    def get_title(self):
        return self.driver.title