from selenium import webdriver
from time import sleep
# import traceback


class AutoBuy(object):
    def __init__(self, url, username, passwd):
        self.url = url
        self.username = username
        self.passwd = passwd
        self.driver = webdriver.Chrome()  # 调用chrome浏览器

    def login(self):
        self.driver.get(self.url)

        # login button
        button = self.driver.find_element_by_class_name('css-1i4id9g')
        print(button, 1111)
        button.click()
        sleep(50)

    def start_buy(self):
        self.login()


if __name__ == '__main__':
    # 有可能跳转中文网站，根据 ip 来的，开启全局代理
    s_url = "https://www.sephora.com/product/diorshow-iconic-overcurl-catwalk-spectacular-makeup-look-set-P441308"
    s_username = 'vincexgliu@gmail.com'
    s_passwd = 'ZAQ1xsw2'
    AutoBuy(s_url, s_username, s_passwd).start_buy()
