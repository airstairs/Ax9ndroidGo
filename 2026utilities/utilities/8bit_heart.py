import subprocess
import os

subprocess.run(["tmux", "new-session", "-d", "-s", "v3"], stderr=subprocess.DEVNULL)

subprocess.run(["tmux", "split-window", "-h", "-t", "v3:0.0"])
subprocess.run(["tmux", "split-window", "-h", "-t", "v3:0.1"])
subprocess.run(["tmux", "split-window", "-h", "-t", "v3:0.0"])
subprocess.run(["tmux", "split-window", "-h", "-t", "v3:0.3"])
subprocess.run(["tmux", "split-window", "-h", "-t", "v3:0.2"])
subprocess.run(["tmux", "split-window", "-h", "-t", "v3:0.1"])
subprocess.run(["tmux", "split-window", "-h", "-t", "v3:0.0"])

subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.0"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.2"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.4"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.6"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.8"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.10"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.12"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.14"])

subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.0"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.3"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.6"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.9"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.12"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.15"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.18"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.21"])

subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.0"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.4"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.8"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.12"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.16"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.20"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.24"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.28"])

subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.3"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.8"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.13"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.18"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.23"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.28"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.33"])
subprocess.run(["tmux", "split-window", "-v", "-t", "v3:0.38"])

session = "v3"
panes_to_target = [18, 23, 7, 12, 22, 27, 32, 17, 1, 6, 11, 16, 21, 26, 31, 36, 5, 10, 25, 30]# etc.

for p in panes_to_target:
    subprocess.run(["tmux", "send-keys", "-t", f"{session}.{p}", "cmatrix -C red -ba", "C-m"])

session = "v3"
panes_to_target = [19,24,13,28, 0,15, 20, 35, 2, 37, 3, 8, 33, 38, 4, 9, 14, 29,34,39]# etc.

for p in panes_to_target:
    subprocess.run(["tmux", "send-keys", "-t", f"{session}.{p}", "cmatrix -C white -m -u 10", "C-m"])

os.system("tmux attach -t v3")





