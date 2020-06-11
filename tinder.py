from tinderUserInfo import email, password,text
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class TinderBot():
    def __init__(self,email,password,text):
        self.text = text
        self.password = password
        self.email = email
        self.driver = webdriver.Chrome()


    def login(self):
        
        self.driver.get("https://tinder.com/")
        time.sleep(4)
        # popup_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        # popup_btn.click()
        # time.sleep(2)
        # login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        # login_btn.click()
        # time.sleep(1)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()
        time.sleep(3)

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(self.email)

        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(self.password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        time.sleep(15)

        self.driver.switch_to_window(base_window)
        self.driver.maximize_window()
        time.sleep(2)

        popup_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_btn.click()
        time.sleep(2)

        popup_btn2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_btn2.click()
        time.sleep(1)

        popup_btn3 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        popup_btn3.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def autoswipe(self):
        while True:
            time.sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.text_match()
                except Exception:
                    self.close_popup()

    def text_match(self):
        popup_text_area = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        popup_text_area.send_keys(self.text)
        time.sleep(1)
        gnder_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button/span')
        gnder_btn.click()
        time.sleep(1)

    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()


        
bot = TinderBot(email,password,text)
bot.login()
bot.autoswipe()