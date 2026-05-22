import os
import time
import math
import shutil

def run_comet():
    step = 0
    speed = 0.1
    refresh_rate = 0.03
    
    # Trail settings: (character, delay_offset)
    # Higher delay_offset means the trail stays further behind
    trail_chars = [("·", 0.3), ("°", 0.2), ("o", 0.1)]

    try:
        while True:
            columns, _ = shutil.get_terminal_size(fallback=(80, 24))
            width = columns - 2
            origin = width // 2
            amplitude = width // 2

            # 1. Create a blank line (buffer) the size of the terminal
            line = [" "] * columns

            # 2. Place the trail characters first
            for char, delay in trail_chars:
                trail_pos = origin + int(amplitude * math.sin(step - delay))
                if 0 <= trail_pos < len(line):
                    line[trail_pos] = char

            # 3. Place the main 'x' (overwrites trail if they overlap)
            main_pos = origin + int(amplitude * math.sin(step))
            if 0 <= main_pos < len(line):
                line[main_pos] = "x"

            # 4. Join the list into a string and print
            print("\r" + "".join(line), end="", flush=True)

            step += speed
            time.sleep(refresh_rate)

    except KeyboardInterrupt:
        print("\n[Comet Stopped]")

if __name__ == "__main__":
    run_comet()
