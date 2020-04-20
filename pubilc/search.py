from pubilc.basepage import Page
import time


class Search(Page):
    def search_box(self):
        return self.by_xpath("//*[@id='keyword']")

    def search_button(self):
        return self.by_xpath("//button[@type='button']")

    def img_commodity(self):
        return self.by_xpath("//a[@id='pdlink1_100002668316']")

    def search(self, value):
        self.open("https://www.yhd.com")
        time.sleep(1)
        self.send_key(webelement=self.search_box(), keys=value)
        self.click(self.search_button())
        self.click(self.img_commodity())
        return SearchPage(self.driver)


class SearchPage(Page):
    def search_title(self):
        self.handle(1)
        return self.get_title()
