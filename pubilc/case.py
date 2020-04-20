import unittest
from pubilc.search import Search
from selenium import webdriver


class YHDtest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        """搜索"""
        value = '卡地亚'
        search_for = Search(driver=self.driver)
        search_page = search_for.search(value)
        text_title = search_page.search_title()
        self.assertIn("瑞士手表", text_title)


if __name__ == '__main__':
    unittest.main()


