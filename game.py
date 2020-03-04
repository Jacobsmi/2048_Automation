from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
import random
import time

class Driver:
    # Constructor creates a new WebDriver object and uses it to open a webpage 
    def __init__(self):
        super().__init__()
        # Creating the driver and passing the location on HDD as an argument
        self.web_driver = webdriver.Chrome('C:/bin/chromedriver')
        # Opens the game in a webpage
        self.web_driver.get("https://play2048.co/")
        actions = ActionChains(self.web_driver)
        actions.send_keys(Keys.UP)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.UP)
        actions.send_keys(Keys.DOWN)
        actions.perform()

    def get_tiles(self):
        # Ensures the page has loaded and prevents stale element errors
        tileWait = WebDriverWait(self.web_driver, 15).until(lambda a: a.find_elements_by_class_name("tile"))
        # Puts any elements with the class name tile into a list called tiles under the form of WebElements
        tiles = self.web_driver.find_elements_by_class_name("tile")
        tiles_info = []
        # Loop through all elements of the list
        for tile in tiles:
            tiles_info.append(tile.get_attribute("class"))
        return tiles_info