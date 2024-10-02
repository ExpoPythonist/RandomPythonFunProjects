import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch the Falling Objects')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
BASKET_WIDTH = 100
BASKET_HEIGHT = 20
OBJECT_SIZE = 20
OBJECT_SPEED = 5
BASKET_SPEED = 10

# Load images
basket_image = pygame.Surface((BASKET_WIDTH, BASKET_HEIGHT))
basket_image.fill(GREEN)
object_image = pygame.Surface((OBJECT_SIZE, OBJECT_SIZE))
object_image.fill(RED)

def draw_basket(x, y):
    SCREEN.blit(basket_image, (x, y))

def draw_object(x, y):
    SCREEN.blit(object_image, (x, y))

def main():
    basket_x = (WIDTH - BASKET_WIDTH) // 2
    basket_y = HEIGHT - BASKET_HEIGHT
    object_x = random.randint(0, WIDTH - OBJECT_SIZE)
    object_y = 0
    score = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= BASKET_SPEED
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - BASKET_WIDTH:
            basket_x += BASKET_SPEED

        # Move object
        object_y += OBJECT_SPEED
        if object_y > HEIGHT:
            object_x = random.randint(0, WIDTH - OBJECT_SIZE)
            object_y = 0

        # Check for collision
        if (basket_x < object_x < basket_x + BASKET_WIDTH or
            basket_x < object_x + OBJECT_SIZE < basket_x + BASKET_WIDTH) and \
            (basket_y < object_y < basket_y + BASKET_HEIGHT or
             basket_y < object_y + OBJECT_SIZE < basket_y + BASKET_HEIGHT):
            score += 1
            object_x = random.randint(0, WIDTH - OBJECT_SIZE)
            object_y = 0

        SCREEN.fill(BLACK)
        draw_basket(basket_x, basket_y)
        draw_object(object_x, object_y)

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
