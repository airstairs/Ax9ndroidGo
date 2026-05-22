import os
import time
import math
import numpy as np

line = ""
size = os.get_terminal_size()

def get_sin_steps(steps, upper_bound):
    results = []
    for k in range(steps + 1):
        angle = (k / steps) * (math.pi / 2)
        val = math.sin(angle) * upper_bound
        results.append(round(val))

    return results

stretch = 30
columns = size.columns - 2
sinstep = get_sin_steps(stretch, columns)
sinsteprev = sinstep[::-1]
sinsteps = sinstep + sinsteprev
go = True
i = 0
length = len(sinsteps)
while go:
    line = "x" * sinsteps[i]
    i += 1
    if i == length:
        i = 0
    #print(line + "x")
    os.system(f"echo \"{line}\" | lolcat")
    time.sleep(0.02)
