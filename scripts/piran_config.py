import sys
import os
import pandas as pd
from time import sleep

breaks_every_n_times = 3
max_loaded = 15000
offset = 0
inns_range = [15, 30]


waits = {
    "long": {
        "std": 20,
        "interval": [5, 15],
        "type": [0.3, 1],
        "mw": 7,
    },
    "medium": {
        "std": 10,
        "interval": [3, 10],
        "type": [0.1, 0.5],
        "mw": 5,
    },
    "fast": {
        "std": 5,
        "interval": [1, 5],
        "type": [0.05, 0.2],
        "mw": 3,
    },
    "fmedium": {
        "std": 5,
        "interval": [3, 10],
        "type": [0.05, 0.2],
        "mw": 3,
    },
}

link_to_bsscdn = "https://247.bsscdn.com/"

login_data = {"login": "admin", "pass": "gnPfDjJKGq"}
dirname = os.path.abspath("")
outdir = os.path.dirname(dirname)
modes = list(waits.keys())

mode = modes[-1]

outpath = os.path.join(outdir, "outputs")
paths = {
    "excels": os.path.join(outpath, "excels"),
    "out": os.path.join(outpath, "out"),
    "out_relatives": os.path.join(outpath, "out_relatives"),
    "inputs": os.path.join(outdir, "inputs"),
}

sys.path.append(dirname)
sys.path.append(os.path.dirname(dirname))
sys.path.append(os.path.dirname(os.path.dirname(dirname)))
