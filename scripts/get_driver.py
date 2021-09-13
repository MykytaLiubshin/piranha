from tqdm import tqdm
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from human_type import human_type
from piran_config import *
from auth import *

def get_driver():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference(
        "browser.download.manager.showWhenStarting", False
    )
    profile.set_preference("browser.download.dir", paths["out"])
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk",
        "application/octet-stream",
    )
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/zip"
    )

    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-extensions")
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    return driver


def get_relative_driver():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference(
        "browser.download.manager.showWhenStarting", False
    )
    profile.set_preference(
        "browser.download.dir", paths["out_relatives"]
    )
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk",
        "application/octet-stream",
    )
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/zip"
    )

    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-extensions")
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    return driver
