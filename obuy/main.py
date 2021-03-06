from selenium import webdriver
from time import sleep
# import traceback


class AutoBuy(object):
    # required params for class, let the be __init__ function params
    # __init__ is a special function of python https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031185408
    def __init__(self, url, username, passwd):
        self.url = url
        self.username = username
        self.passwd = passwd
        # call chrome browser
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.url)

        # locating element - https://selenium-python.readthedocs.io/locating-elements.html
        # xpath is general method
        # login button
        button = self.driver.find_element_by_class_name('css-1i4id9g')
        print(button, 1111)
        button.click()

        # navigating - choose popup https://selenium-python.readthedocs.io/navigating.html#popup-dialogs
        # this means change current window? https://blog.csdn.net/Eastmount/article/details/77074306
        # login dialog
        alert = self.driver.switch_to_alert()
        print(alert)
        sleep(50)

    def start_buy(self):
        self.login()


# how to undertand __name__ == '__main__':https://www.zhihu.com/question/49136398
if __name__ == '__main__':
    # if jump to chinese website, just open global proxy
    s_url = "https://www.sephora.com/product/diorshow-iconic-overcurl-catwalk-spectacular-makeup-look-set-P441308"
    s_username = ''
    s_passwd = ''
    AutoBuy(s_url, s_username, s_passwd).start_buy()
