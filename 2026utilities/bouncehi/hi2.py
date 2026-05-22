import os
import time
import math

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
        
            print(" " * pos + "x", end="\r", flush=True)

            i += 1
            time.sleep(speed)
try:
    oscillate()
except KeyboardInterrupt:
    print("\nStopped.")
