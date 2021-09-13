import sys
import os
import subprocess as s
from datetime import date, timedelta

dirname = os.path.abspath("")
outdir = os.path.dirname(dirname)


if __name__ == "__main__":
    yesterday = date.today() - timedelta(days=1)
    dname = f"_{yesterday.day}_{yesterday.month}_{yesterday.year}"
    try:
        s.run(
            f"cd .. && cd old && mkdir {dname}", shell=True, check=True
        )
    except Exception as e:
        print(e)

    try:
        s.run(
            f"cd .. && cd outputs && dir && cp excels ./../old/{dname}/ && cp out ./../old/{dname}/ && cp out_relatives ./../old/{dname}/",
            shell=True,
            check=True,
        )
    except Exception as e:
        print(e)
