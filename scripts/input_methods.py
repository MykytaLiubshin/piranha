import os
import sys
from time import sleep
from tqdm import tqdm
import random as r
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from human_type import human_type
from piran_config import *

def input_inn(driver, INN="3230509750", std_timeout=waits[mode]["std"]):
    base = "#inn_content > p\\:filterblock:nth-child(1) > p\\:actionblock:nth-child(2) > p\\:actionbox:nth-child(1) >"
    clear_css = f"{base} p\\:abutton:nth-child(2) > span:nth-child(1)"

    clear_field = WebDriverWait(driver, std_timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, clear_css))
    )
    clear_field.click()

    inn_search_css = ".formTable > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1) > input:nth-child(1)"

    inn_search_field = WebDriverWait(driver, std_timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, inn_search_css))
    )

    human_type(driver, inn_search_field, INN)

    inn_search_button_css = (
        f"{base} p\\:abutton:nth-child(3) > span:nth-child(1)"
    )
    inn_search_button = WebDriverWait(driver, std_timeout).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, inn_search_button_css)
        )
    )
    inn_search_button.click()

    sleep(waits[mode]["mw"])


def personal_data_open(driver):
    personal_data_css = "p\\:subdatablock.cAB:nth-child(4) > p\\:c3:nth-child(1) > p\\:c4:nth-child(1) > p\\:subdatabox:nth-child(1) > p\\:sdtabswitches:nth-child(1) > p\\:sdtswitch:nth-child(1) > b:nth-child(1) > span:nth-child(1)"
    personal_data_button = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, personal_data_css))
    )
    sleep(r.uniform(*waits[mode]["interval"]))
    personal_data_button.click()
    sleep(r.uniform(*waits[mode]["interval"]))

    download_button_css = (
        ".sdActionBox > p\\:abutton:nth-child(1) > span:nth-child(1)"
    )
    download_button = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, download_button_css)
        )
    )
    sleep(waits[mode]["std"])
    download_button.click()
    sleep(waits[mode]["mw"])


def relatives_to_excels(driver, inn, std_timeout=waits[mode]["std"]):
    sleep(r.uniform(*waits[mode]["interval"]))

    try:
        df = pd.DataFrame()
        all_d = driver.find_elements_by_tag_name("a")
        for i in all_d:
            if i.text.isdigit() and len(i.text) == len("1234567890"):
                df = df.append(
                    {"Main": inn, "Relative": i.text}, ignore_index=True
                )

        df.to_excel(
            os.path.join(paths["excels"], f"{inn}_relatives.xlsx")
        )
    except Exception as e:
        print(e)


def download_data(driver):
    sleep(waits[mode]["mw"])
    save_button_css = "p\:msgblock:nth-child(1) > p\:c1:nth-child(1) > p\:c2:nth-child(1) > p\:c3:nth-child(1) > p\:c4:nth-child(1) > div:nth-child(1)"
    save_button = WebDriverWait(driver, waits[mode]["std"]).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, save_button_css))
    )
    sleep(waits[mode]["mw"])
    try:
        sleep(waits[mode]["mw"])
        links = save_button.find_elements_by_tag_name("a")
        for i in links:
            if "pdf" in i.text:
                i.click()
                sleep(waits[mode]["mw"])
    except Exception as e:
        print(e)
