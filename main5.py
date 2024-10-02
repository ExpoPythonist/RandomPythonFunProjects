import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Ball:
    def __init__(self, position, velocity, radius):
        self.position = position
        self.velocity = velocity
        self.radius = radius

    def update_position(self, dt):
        self.position += self.velocity * dt

    def check_collision_with_wall(self, width, height):
        # Check collision with walls and update velocity accordingly
        if self.position[0] - self.radius < 0 or self.position[0] + self.radius > width:
            self.velocity[0] *= -1
        if self.position[1] - self.radius < 0 or self.position[1] + self.radius > height:
            self.velocity[1] *= -1

    def check_collision_with_ball(self, other_ball):
        # Check collision with another ball and update velocities
        if np.linalg.norm(self.position - other_ball.position) <= self.radius + other_ball.radius:
            # Elastic collision formula
            v1, v2 = self.velocity, other_ball.velocity
            m1, m2 = 1, 1  # Assuming equal mass for simplicity
            new_v1 = v1 - 2 * m2 / (m1 + m2) * np.dot(v1 - v2, self.position - other_ball.position) / np.linalg.norm(self.position - other_ball.position)**2 * (self.position - other_ball.position)
            new_v2 = v2 - 2 * m1 / (m1 + m2) * np.dot(v2 - v1, other_ball.position - self.position) / np.linalg.norm(other_ball.position - self.position)**2 * (other_ball.position - self.position)
            self.velocity = new_v1
            other_ball.velocity = new_v2

def update(frame):
    global balls, ax, width, height, dt

    for ball in balls:
        ball.update_position(dt)
        ball.check_collision_with_wall(width, height)
        for other_ball in balls:
            if ball != other_ball:
                ball.check_collision_with_ball(other_ball)

    ax.clear()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    for ball in balls:
        circle = plt.Circle((ball.position[0], ball.position[1]), ball.radius, color='blue')
        ax.add_patch(circle)

# Initialize parameters
num_balls = 5
width, height = 10, 10
dt = 0.05  # Time step for simulation

# Create balls with random initial positions and velocities
balls = []
for _ in range(num_balls):
    position = np.random.rand(2) * width
    velocity = (np.random.rand(2) - 0.5) * 2  # Random initial velocity
    radius = np.random.rand() * 0.5 + 0.5  # Random radius between 0.5 and 1.0
    balls.append(Ball(position, velocity, radius))

# Create figure and axes for visualization
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)

# Animate the simulation
ani = FuncAnimation(fig, update, frames=200, interval=50, repeat=False)
plt.show()
