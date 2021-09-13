from tqdm import tqdm
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from human_type import human_type
from piran_config import *


def auth(driver):
    driver.get(link_to_bsscdn)
    login_field_xpass = '//*[@id="userInputText"]'
    login_field = WebDriverWait(driver, waits[mode]["std"]).until(
        EC.element_to_be_clickable((By.XPATH, login_field_xpass))
    )
    human_type(driver, login_field, login_data["login"])

    password_field = WebDriverWait(driver, waits[mode]["std"]).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".formTable > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)",
            )
        )
    )
    human_type(driver, password_field, login_data["pass"])
    # password_field.submit()
    sleep(1)

    in_button_field = WebDriverWait(driver, waits[mode]["std"]).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".rAlign > p\\:abutton:nth-child(2) > span:nth-child(1)",
            )
        )
    )
    in_button_field.click()


def unauth(driver):
    try:
        exit_button_class = "exitButton"
        exit_button = WebDriverWait(driver, waits[mode]["std"]).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, exit_button_class)
            )
        )
        exit_button.click()

    except Exception as e:
        print(e)
