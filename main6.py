import pygame
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('School of Fish Simulation')

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Fish:
    def __init__(self, position, velocity, size):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.size = size

    def update_position(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.position[0]), int(self.position[1])), self.size)

def simulate_fish(num_fish):
    fish = []
    for _ in range(num_fish):
        position = [random.randint(0, width), random.randint(0, height)]
        velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        size = random.randint(5, 15)
        fish.append(Fish(position, velocity, size))
    return fish

def update_fish(fish):
    for f in fish:
        # Simple flocking behavior: move towards center of mass of neighbors
        center_of_mass = np.zeros(2)
        separation = np.zeros(2)
        for other in fish:
            if other != f:
                distance = np.linalg.norm(f.position - other.position)
                if distance < 50:
                    separation += (f.position - other.position) / distance**2
                    center_of_mass += other.position
        if len(fish) > 1:
            center_of_mass /= (len(fish) - 1)
            f.velocity += 0.1 * (center_of_mass - f.position) / np.linalg.norm(center_of_mass - f.position)
            f.velocity += 0.1 * separation

        # Update position
        f.update_position(1)

def draw(screen, fish):
    screen.fill(WHITE)
    for f in fish:
        f.draw(screen)
    pygame.display.flip()

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    fish = simulate_fish(30)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_fish(fish)
        draw(screen, fish)
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
