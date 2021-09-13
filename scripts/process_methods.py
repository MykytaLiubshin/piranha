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
from auth import *
from get_driver import *
from input_methods import *

def process_mains(data, n = 0):
    if n == -1:
        sleep(60*r.randint(*waits[mode]['interval']))
    
    inns = data
    d = get_driver()
    auth(d)
    for inn in tqdm(inns):
        try:
            input_inn(d, str(inn))
            personal_data_open(d)
            download_data(d)
            relatives_to_excels(d,str(inn), 10 )
        except Exception as e:
            print(e)
    unauth(d)
    d.close()
    d.quit()

def process_relatives(data, n = 0, d = None):
    if n == -1:
        sleep(60*r.randint(*waits[mode]['interval']))
    d = get_relative_driver()
    df = []
    mains = []
    for i in data:
        try:
            fl = pd.read_excel(os.path.join(paths['excels'], f"{i}_relatives.xlsx"))
            df.extend(fl['Relative'][:10])
            mains.extend(fl['Main'][:10])
        except Exception as e:
            pass

    r.shuffle(df)
    df = list(filter( lambda x: x not in mains , df))

    inns = df

    d = get_relative_driver()
    auth(d)
    for inn in tqdm(inns):
        try:
            input_inn(d, str(inn))
            personal_data_open(d)
            download_data(d)
            sleep(r.uniform(*waits[mode]['interval']))
        except Exception as e:
            print(e)
    unauth(d)
    d.close()
    d.quit()
