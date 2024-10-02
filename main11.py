import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
GROUND_HEIGHT = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Game variables
gravity = 1
dino_vel = 0
jumping = False
game_over = False

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

# Function to draw text on screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Main game loop
def main():
    global dino_vel, jumping, game_over

    dino_size = 40
    dino_pos = [100, SCREEN_HEIGHT - GROUND_HEIGHT - dino_size]

    obstacle_width = 20
    obstacle_height = random.randint(20, 60)
    obstacle_x = SCREEN_WIDTH
    obstacle_y = SCREEN_HEIGHT - GROUND_HEIGHT - obstacle_height

    score = 0
    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jumping and not game_over:
                    jumping = True
                    dino_vel = -15
                elif event.key == pygame.K_RETURN and game_over:
                    # Reset game variables
                    dino_pos = [100, SCREEN_HEIGHT - GROUND_HEIGHT - dino_size]
                    obstacle_x = SCREEN_WIDTH
                    obstacle_height = random.randint(20, 60)
                    obstacle_y = SCREEN_HEIGHT - GROUND_HEIGHT - obstacle_height
                    score = 0
                    game_over = False

        if not game_over:
            # Update dino position
            if jumping:
                dino_vel += gravity
                dino_pos[1] += dino_vel
                if dino_pos[1] >= SCREEN_HEIGHT - GROUND_HEIGHT - dino_size:
                    dino_pos[1] = SCREEN_HEIGHT - GROUND_HEIGHT - dino_size
                    jumping = False

            # Update obstacle position
            obstacle_x -= 10
            if obstacle_x < -obstacle_width:
                obstacle_x = SCREEN_WIDTH
                obstacle_height = random.randint(20, 60)
                obstacle_y = SCREEN_HEIGHT - GROUND_HEIGHT - obstacle_height
                score += 1

            # Check collision
            if (dino_pos[0] + dino_size > obstacle_x and dino_pos[0] < obstacle_x + obstacle_width and
                dino_pos[1] + dino_size > obstacle_y):
                game_over = True

        # Draw everything
        screen.fill(WHITE)
        
        # Draw dinosaur (rectangle)
        pygame.draw.rect(screen, (255, 0, 0), [dino_pos[0], dino_pos[1], dino_size, dino_size])

        # Draw obstacle (rectangle)
        pygame.draw.rect(screen, (0, 255, 0), [obstacle_x, obstacle_y, obstacle_width, obstacle_height])
        
        if game_over:
            draw_text("Game Over!", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
            draw_text(f"Score: {score}", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
            draw_text("Press Enter to Play Again", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        else:
            draw_text(f"Score: {score}", font, BLACK, screen, SCREEN_WIDTH // 2, 20)

        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
