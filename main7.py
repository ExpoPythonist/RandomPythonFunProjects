import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game')

# Paddle A
paddle_a_x = 50
paddle_a_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Paddle B
paddle_b_x = SCREEN_WIDTH - 50 - PADDLE_WIDTH
paddle_b_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball
ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
ball_speed_x = BALL_SPEED_X * random.choice([-1, 1])
ball_speed_y = BALL_SPEED_Y * random.choice([-1, 1])

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a_y > 0:
        paddle_a_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        paddle_a_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b_y > 0:
        paddle_b_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        paddle_b_y += PADDLE_SPEED

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top/bottom walls
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball_x <= paddle_a_x + PADDLE_WIDTH and paddle_a_y <= ball_y + BALL_SIZE <= paddle_a_y + PADDLE_HEIGHT:
        ball_speed_x = -ball_speed_x
    if ball_x >= paddle_b_x - BALL_SIZE and paddle_b_y <= ball_y + BALL_SIZE <= paddle_b_y + PADDLE_HEIGHT:
        ball_speed_x = -ball_speed_x

    # Ball out of bounds (score)
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
        ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = BALL_SPEED_X * random.choice([-1, 1])
        ball_speed_y = BALL_SPEED_Y * random.choice([-1, 1])

    # Clear screen
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (paddle_a_x, paddle_a_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle_b_x, paddle_b_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Update screen
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
