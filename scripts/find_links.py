import os
import sys
import random as r

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from human_type import human_type


def sleep(t):
    print(f"sleeping for {t} secs")
    return sleep(t)


dirname = os.path.abspath("")

sys.path.append(dirname)
sys.path.append(os.path.dirname(dirname))
sys.path.append(os.path.dirname(os.path.dirname(dirname)))


def auth(driver):
    driver.get("https://247.bsscdn.com/")
    login_field_xpass = '//*[@id="userInputText"]'
    login_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, login_field_xpass))
    )
    human_type(driver, login_field, "admin")
    # sleep(4)
    password_field_xpass = "//p:logincontentblock/p:logincontentbox/p:loginplateblock/p:loginplatebox/form/p:logincol1/p:plateblock/p:c1/p:c2/p:c3/p:c4/p:formblock/table/tbody/tr[2]/td/input"
    password_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".formTable > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)",
            )
        )
    )
    human_type(driver, password_field, "gnPfDjJKGq")
    # password_field.submit()
    sleep(4)

    in_button = "//p:logincontentblock/p:logincontentbox/p:loginplateblock/p:loginplatebox/form/p:logincol1/p:actionblock/p:actionbox/p:abutton/span"
    in_button_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".rAlign > p\\:abutton:nth-child(2) > span:nth-child(1)",
            )
        )
    )
    in_button_field.click()


def input_inn(driver, INN="3230509750"):
    inn_search_css = ".formTable > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1) > input:nth-child(1)"

    inn_search_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, inn_search_css))
    )

    human_type(driver, inn_search_field, INN)
    # inn_search_field.submit()
    inn_search_button_css = "#inn_content > p\\:filterblock:nth-child(1) > p\\:actionblock:nth-child(2) > p\\:actionbox:nth-child(1) > p\\:abutton:nth-child(3) > span:nth-child(1)"
    inn_search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, inn_search_button_css)
        )
    )
    inn_search_button.click()

    sleep(10)


def personal_data_open(driver):
    personal_data_css = "p\\:subdatablock.cAB:nth-child(4) > p\\:c3:nth-child(1) > p\\:c4:nth-child(1) > p\\:subdatabox:nth-child(1) > p\\:sdtabswitches:nth-child(1) > p\\:sdtswitch:nth-child(1) > b:nth-child(1) > span:nth-child(1)"
    personal_data_button = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, personal_data_css))
    )
    sleep(r.uniform(3, 12))
    personal_data_button.click()
    sleep(r.randint(5, 15))

    download_button_css = (
        ".sdActionBox > p\\:abutton:nth-child(1) > span:nth-child(1)"
    )
    download_button = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, download_button_css)
        )
    )
    sleep(r.uniform(5, 15))
    download_button.click()
    sleep(r.uniform(5, 15))
    save_button_css = "#sh_fa_16766824371877182200 > p\\:msgblock:nth-child(1) > p\\:c1:nth-child(1) > p\\:c2:nth-child(1) > p\\:c3:nth-child(1) > p\\:c4:nth-child(1) > div:nth-child(1) > p\\:msgtext:nth-child(2) > a:nth-child(3)"
    save_button = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, save_button_css))
    )
    sleep(r.uniform(1, 10))
    save_button.click()
    sleep(r.uniform(1, 10))


def find_data_and_buttons(INN):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference(
        "browser.download.manager.showWhenStarting", False
    )
    profile.set_preference(
        "browser.download.dir",
        "C:\\Users\\piran\\Desktop\\Piran\\ParserSelenium\\out",
    )

    options = webdriver.FirefoxOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Firefox(options=options, firefox_profile=profile)

    auth(driver)
    input_inn(driver)
    personal_data_open(driver)
    # sleep(10000)


find_data_and_buttons(1)
