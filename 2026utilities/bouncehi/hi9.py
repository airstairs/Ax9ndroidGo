import os
import time
import math
import numpy as np

def oscillate():
        size = os.get_terminal_size()
        # Columns - 2 to prevent wrapping; 'origin' is the center of the screen
        columns = size.columns - 2
        origin = columns // 2
        amplitude = columns // 2

        # Increase 'steps' for a smoother movement, 
        # increase 'speed' to make it move faster0
        steps = 60
        speed = 0.05

        i = 0
        while True:
            # We use 2 * pi to complete a full, smooth circle
            angle = (i / steps) * (2 * math.pi)
        
            # Calculate offset from center (origin)
            # Offset will swing between -amplitude and +amplitude
            offset = int(amplitude * math.sin(angle))
                                                                                                                    
            # Final position relative to the middle
            pos = origin + offset
        
            print(" " * pos + "x")

            i += 1
            time.sleep(speed)
            ran = np.random.randint(10)
            if ran < 4:
                time.sleep(0.04)
            elif ran < 7:
                time.sleep(0.2)
            elif ran < 9:
                time.sleep(0.08)
try:
    oscillate()
except KeyboardInterrupt:
    print("\nStopped.")
