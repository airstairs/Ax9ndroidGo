import os
import time
import math
import shutil

def run_oscillation():
    """
    Smoothly oscillates an 'x' around the center of the terminal
    using a sine wave.
    """
    step = 0
    # Increase this to make the movement faster
    speed = 0.1 
    # Adjust for smoothness (lower = more frames per second)
    refresh_rate = 0.03

    try:
        while True:
            # 1. Get current terminal width (dynamic if resized)
            columns, _ = shutil.get_terminal_size(fallback=(80, 24))
            
            # 2. Define the '1' axis (the middle)
            # Subtracting 2 to account for the character and the edge
            width = columns - 2
            origin = width // 2
            amplitude = width // 2
            
            # 3. Calculate position using the full Sine circle
            # sin(step) goes from -1 to 1
            offset = int(amplitude * math.sin(step))
            pos = origin + offset
            
            # 4. Print with \r to stay on one line and flush to bypass buffer
            # The ' ' * pos creates the leading whitespace
            print(f"\r{' ' * pos}x", end="", flush=True)
            
            step += speed
            time.sleep(refresh_rate)

    except KeyboardInterrupt:
        # Clean exit to move cursor to a new line
        print("\n[Animation Stopped]")

if __name__ == "__main__":
    run_oscillation()
