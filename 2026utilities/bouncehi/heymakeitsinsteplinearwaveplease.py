import os
import time
import math
import numpy as np

go = True
i = 0

while go:

    size = os.get_terminal_size()
    columns = size.columns - 2
    line = " " * 2*i
    i += 1
    if i == columns:
        i = 0
    print(line + "x")
    time.sleep(0.02)
