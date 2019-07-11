import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_path = "/Users/param/AppData/Local/Programs/Python/Python37/chromedriver.exe"


class MyTwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(chrome_path)

    def login(self):
        driver = self.bot
        driver.get('https://twitter.com/')
        time.sleep(3)
        email = driver.find_element_by_name('session[username_or_email]')
        password = driver.find_element_by_name('session[password]')
        email.send_keys(self.username)
        password.send_keys(self.password)
        driver.find_element_by_xpath(
            '//*[@id="doc"]/div/div[1]/div[1]/div[1]/form/input[1]').submit()
        time.sleep(3)

    def like_tweet(self, hashtag):
        driver = self.bot
        driver.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1, 3):
            driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = driver.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            print(links)
            for link in links:
                driver.get('https://twitter.com'+link)
                try:
                    heartbutton = driver.find_element_by_class_name(
                        'HeartAnimation')
                    heartbutton.click()
                    time.sleep(5)
                except Exception as ex:
                    time.sleep(5)


def main():
    hashtag = input("What hashtag you want to like?")
    MyTwitterBotInstance = MyTwitterBot(
        '', '')
    MyTwitterBotInstance.login()
    MyTwitterBotInstance.like_tweet(hashtag)


main()
