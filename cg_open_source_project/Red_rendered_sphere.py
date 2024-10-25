import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Sphere with Obstacles")

# Define colors
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)  # Light blue background
BLACK = (255, 255, 255)

# Set initial position, radius, and velocity
x, y = WIDTH // 2, HEIGHT // 2
radius = 20
velocity_x, velocity_y = 3, 3

# Define obstacles (rectangles)
obstacles = [
    pygame.Rect(200, 150, 100, 300),  # x, y, width, height
    pygame.Rect(500, 100, 150, 50),
    pygame.Rect(300, 400, 200, 30)
]

# Function to detect collision between the sphere and a rectangle
def check_collision(circle_x, circle_y, radius, rect):
    # Closest point on the rectangle to the circle
    closest_x = max(rect.left, min(circle_x, rect.right))
    closest_y = max(rect.top, min(circle_y, rect.bottom))

    # Calculate the distance between the circle and this closest point
    distance_x = circle_x - closest_x
    distance_y = circle_y - closest_y

    # If the distance is less than the radius, a collision has occurred
    return math.sqrt(distance_x**2 + distance_y**2) < radius

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position with bouncing logic for window edges
    if x + radius >= WIDTH or x - radius <= 0:
        velocity_x *= -1
    if y + radius >= HEIGHT or y - radius <= 0:
        velocity_y *= -1

    # Check for collisions with each obstacle
    for rect in obstacles:
        if check_collision(x, y, radius, rect):
            # Reverse direction upon collision
            if x < rect.left or x > rect.right:
                velocity_x *= -1
            if y < rect.top or y > rect.bottom:
                velocity_y *= -1

    # Update sphere position
    x += velocity_x
    y += velocity_y

    # Clear screen with light blue background
    window.fill(LIGHT_BLUE)

    # Draw obstacles (black rectangles)
    for rect in obstacles:
        pygame.draw.rect(window, BLACK, rect)

    # Draw the red sphere
    pygame.draw.circle(window, RED, (x, y), radius)

    # Update display
    pygame.display.flip()

    # Control the frame rate
    time.sleep(0.01)

# Quit Pygame
pygame.quit()
