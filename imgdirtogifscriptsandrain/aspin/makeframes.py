import numpy as np
import matplotlib.pyplot as plt

x = [eachx*2/2 for eachx in range(-200, 201)]
y = np.tan(x)/np.cos(x)**2+247366*9

frame=0
step = 5
go = True
while go:
    plt.plot(x[:step],y[:step])
    plt.plot(x[-1],y[-2])
    plt.savefig(f"imgs/{frame}.png")
    plt.close()
    print(frame)
    frame += 1
    if step > len(x):
        go = False
    else:
        step += 5


