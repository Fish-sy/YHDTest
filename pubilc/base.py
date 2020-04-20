from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Action:
    def __init__(self, browser, driver):
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'ie' or 'internet explorer':
            driver = webdriver.Ie()
        elif browser == 'firefox' or 'ff':
            driver = webdriver.Firefox()
        try:
            self.driver = driver
        except Exception:
            raise NameError('没有找到浏览器')

    def wait(self, sec=10):
        self.driver.implicitly_wait(sec)

    def max_window(self):
        self.driver.maximize_window()

    def to_element(self, key):
        if '->' not in key:
            raise NameError('参数类型输入错误')
        by = key.split('->')[0]
        val = key.split('->')[1]
        # by = key
        # val = value
        if by == 'id':
            element = self.driver.find_element_by_id(val)
        elif by == 'name':
            element = self.driver.find_element_by_name(val)
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(val)
        elif by == 'calss':
            element = self.driver.find_element_by_class_name(val)
        elif by == 'link_text':
            element = self.driver.find_element_by_link_text(val)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(val)
        else:
            raise NameError('请输入正确的定位方式')
        return element

    def open(self, url):
        self.driver.get(url)

    def clear(self, key):
        el = self.to_element(key)
        el.clear()

    def input(self, key, text):
        el = self.to_element(key)
        el.send_keys(text)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def click(self, key):
        el = self.to_element(key)
        el.click()

    def right_click(self, key):
        el = self.to_element(key)
        ActionChains(self.driver).context_click(el).perform()

    def double_click(self, key):
        el = self.to_element(key)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_key, ta_key):
        el = self.to_element(el_key)
        target = self.to_element(ta_key)
        ActionChains(self.driver).drag_and_drop(el, target).perform()

    def move_to_element(self, key):
        el = self.to_element(key)
        ActionChains(self.driver).move_to_element(el).perform()

    def submit(self, key):
        el = self.to_element(key)
        el.submit()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_attribute(self, key, attribute):
        el = self.to_element(key)
        return el.get_attribute(attribute)

    def get_text(self, key):
        el = self.to_element(key)
        return el.text

    def to_frame(self, key):
        el = self.to_element(key)
        self.driver.switch_to.frame(el)

    # 对话框确认操作
    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    # 对话框取消操作
    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    # 截图
    def img(self, fp):
        self.driver.get_screenshot_as_file(fp)

    # 下拉框操作
    def select_by_value(self, key, value):
        el = self.to_element(key)
        Select(el).select_by_value(value)

    # 执行js
    def js(self, script):
        self.driver.execute_script(script)














































