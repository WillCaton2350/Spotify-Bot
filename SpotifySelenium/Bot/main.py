from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from States.data import url, geckoDriverPath
from States.data import username_xpath
from selenium.webdriver.common.by import By
from selenium import webdriver as web
from urllib.error import HTTPError
from States.data import searchBar
import pyautogui as py_gui
import time
import os

class spotifyBot:
    def __init__(self):
        self.driver = None
    def startDriver(self):
        firefox_options = web.FirefoxOptions()
        self.driver = web.Firefox(
            options=firefox_options
        )
        os.environ[
            "webdriver.firefox.driver"
            ] =  geckoDriverPath
        self.driver.maximize_window()
    def startBrowser(self):
        self.driver.get(url)
        try:
            WDW(self.driver, 10).until(ec.url_to_be(url))
            time.sleep(7)
        except HTTPError as err:
            print(err)

    def login(self):
        py_gui.moveTo(570,746)
        time.sleep(1)
        py_gui.click()
        print('clicked')
        time.sleep(10)
        py_gui.moveTo(638,724)
        time.sleep(1)
        py_gui.click()
        print('clicked')
        time.sleep(10)

    def runBot(self):
        try:
            WDW(self.driver, 10).until(
                ec.presence_of_element_located((
                    By.XPATH,
                        searchBar
                )))
            time.sleep(2)
            self.driver.find_element(
                By.XPATH,
                searchBar).send_keys(
                    "Usher")
            print("Typed")
            time.sleep(1)
            action = ac(self.driver)
            action.send_keys(Keys.ENTER)
            time.sleep(1)
            action.perform()
            print("pressed")
            time.sleep(2)
            py_gui.moveTo(
                724,489
            )
            time.sleep(1)
            py_gui.click()
            print('clicked')
            time.sleep(10)
        except NoSuchElementException as err:
            print(err)
    def cursor_coor(self):
        py_gui.moveTo(
           393,484
        )
        time.sleep(3)
        py_gui.click()
        print('clicked play button')
        time.sleep(20)
    def closeDriver(self):
        self.driver.close()
