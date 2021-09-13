from selenium import webdriver
from piran_config import waits


def human_type(driver, elem, text):
    for character in text:
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(elem)
        elem.click()
        actions.send_keys(character)
        actions.perform()
