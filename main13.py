import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Parameters
num_frames = 100
x = np.linspace(-1, 1, num_frames)
y = np.sin(2 * np.pi * x)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Set up the line object
line, = ax.plot([], [], lw=2)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Bouncing Ball Animation')

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    y_data = np.sin(2 * np.pi * (x + frame / num_frames))
    line.set_data(x, y_data)
    return line,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
