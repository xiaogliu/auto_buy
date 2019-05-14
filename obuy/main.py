from selenium import webdriver
from time import sleep
# import traceback


class AutoBuy(object):
    # required params for class, let the be __init__ function params
    # __init__ is a special function of python
    def __init__(self, url, username, passwd):
        self.url = url
        self.username = username
        self.passwd = passwd
        # call chrome browser
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.url)

        # locating element - https://selenium-python.readthedocs.io/locating-elements.html
        # login button
        button = self.driver.find_element_by_class_name('css-1i4id9g')
        print(button, 1111)
        button.click()

        # navigating - choose popup https://selenium-python.readthedocs.io/navigating.html#popup-dialogs
        # login dialog
        alert = self.driver.switch_to_alert()
        print(alert)
        sleep(50)

    def start_buy(self):
        self.login()


if __name__ == '__main__':
    # if jump to chinese website, just open global proxy
    s_url = "https://www.sephora.com/product/diorshow-iconic-overcurl-catwalk-spectacular-makeup-look-set-P441308"
    s_username = 'vincexgliu@gmail.com'
    s_passwd = 'ZAQ1xsw2'
    AutoBuy(s_url, s_username, s_passwd).start_buy()
