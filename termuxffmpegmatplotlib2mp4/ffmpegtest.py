import matplotlib
matplotlib.use('Agg')  # Required for headless environments like Termux
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 1. Setup the figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# 2. Define the update function
def update(frame):
    # Update the data for each frame
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

# 3. Create the animation object
# frames=100 defines how many images to render
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# 4. Save the output
print("Rendering animation... this may take a moment.")
ani.save('graph_animation.mp4', writer='ffmpeg', fps=30)
print("Done! Saved as graph_animation.mp4")