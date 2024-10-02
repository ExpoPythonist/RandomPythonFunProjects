import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodger Game")

# Clock to control the game speed
clock = pygame.time.Clock()

# Player attributes
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - 2 * player_size
player_speed = 7

# Obstacle attributes
obstacle_size = 50
obstacle_speed = 5
obstacle_list = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Functions
def draw_player(x, y):
    pygame.draw.rect(screen, black, [x, y, player_size, player_size])

def draw_obstacle(x, y):
    pygame.draw.rect(screen, red, [x, y, obstacle_size, obstacle_size])

def display_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

def collision(player_x, player_y, obstacle_x, obstacle_y):
    if player_x + player_size > obstacle_x and player_x < obstacle_x + obstacle_size:
        if player_y + player_size > obstacle_y and player_y < obstacle_y + obstacle_size:
            return True
    return False

# Game loop
running = True
while running:
    screen.fill(white)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Spawn obstacles
    if len(obstacle_list) < 10:
        obstacle_x = random.randrange(0, screen_width - obstacle_size)
        obstacle_y = random.randrange(-screen_height, 0)
        obstacle_list.append([obstacle_x, obstacle_y])

    # Move and draw obstacles
    for obstacle in obstacle_list:
        obstacle[1] += obstacle_speed
        draw_obstacle(obstacle[0], obstacle[1])

        # Check collision
        if collision(player_x, player_y, obstacle[0], obstacle[1]):
            running = False

        # Remove obstacles that have gone off screen
        if obstacle[1] > screen_height:
            obstacle_list.remove(obstacle)
            score += 1

    # Draw the player
    draw_player(player_x, player_y)

    # Display score
    display_score(score)

    # Update the screen
    pygame.display.update()

    # Control game speed
    clock.tick(30)

# Quit Pygame
pygame.quit()
