import os
from tqdm import tqdm
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from human_type import human_type
from piran_config import *
from process_methods import *


def orchestra():
    chunks = []

    data = pd.read_excel(os.path.join(paths["inputs"], "data.xlsx"))[
        "INN"
    ][offset:]

    i, j = 0, len(data)

    while i < j:
        k = 20
        chunks.append(data[i : i + k])
        i += k

    for n in range(len(chunks)):
        print(f"{n}. {len(chunks[n])} ІПН. ")
        data_piece = chunks[n]
        if n % breaks_every_n_times == 0 and n != 0:
            process_mains(data_piece, -1)
            process_relatives(data_piece)
        else:
            process_mains(data_piece)
            process_relatives(data_piece)

if __name__ == "__main__":
    orchestra()
