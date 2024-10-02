import pygame
import colorsys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors (RGB format)
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Color Wheel - Color Theory Visualization")
clock = pygame.time.Clock()

# Function to convert HSV to RGB
def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

# Function to generate color harmonies
def generate_color_harmonies(base_color):
    harmonies = []

    # Complementary color
    complementary_hue = (base_color[0] / 255.0 + 0.5) % 1.0
    complementary_color = hsv_to_rgb(complementary_hue, 1.0, 1.0)
    harmonies.append(complementary_color)

    # Analogous colors (±30 degrees)
    analogous_hues = [(base_color[0] / 255.0 + i * 30 / 360.0) % 1.0 for i in range(-1, 2)]
    analogous_colors = [hsv_to_rgb(hue, 1.0, 1.0) for hue in analogous_hues]
    harmonies.extend(analogous_colors)

    # Triadic colors (±120 degrees)
    triadic_hues = [(base_color[0] / 255.0 + i * 120 / 360.0) % 1.0 for i in range(3)]
    triadic_colors = [hsv_to_rgb(hue, 1.0, 1.0) for hue in triadic_hues]
    harmonies.extend(triadic_colors)

    return harmonies

# Main loop
running = True
while running:
    screen.fill(white)

    # Get mouse position and draw color wheel with harmonies
    mouse_x, mouse_y = pygame.mouse.get_pos()
    hue = mouse_x / screen_width  # Hue based on mouse position
    base_color = hsv_to_rgb(hue, 1.0, 1.0)
    color_harmonies = generate_color_harmonies(base_color)

    # Draw color wheel
    pygame.draw.circle(screen, base_color, (screen_width // 2, screen_height // 2), 200)

    # Draw harmonies
    angle_increment = 360 / len(color_harmonies)
    for i, color in enumerate(color_harmonies):
        angle = i * angle_increment
        x = int(screen_width // 2 + 200 * pygame.math.Vector2(1, 0).rotate(angle)[0])
        y = int(screen_height // 2 + 200 * pygame.math.Vector2(1, 0).rotate(angle)[1])
        pygame.draw.circle(screen, color, (x, y), 50)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
