#!/bin/bash

# 1. Start a new detached tmux session named 'cube'
tmux new-session -d -s cube

# 2. Send the 'cd' command to the session
tmux send-keys -t cube "cd /storage/emulated/0/x/Ax9ndroidGo/3dprogramming" C-m

# 3. Send the command to spin up the Python HTTP server
# Note: In Python 3, the module is 'http.server'
tmux send-keys -t cube "python -m http.server" C-m

# 4. Attach to your freshly created session
tmux attach-session -t cube
