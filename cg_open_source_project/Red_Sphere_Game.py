import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paddle Ball Game")

# Define colors
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game constants
radius = 20
ball_speed_x = 4
ball_speed_y = 4
paddle_width = 100
paddle_height = 15
paddle_speed = 8

# Initial positions
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - paddle_height - 10  # Paddle positioned at the bottom of the screen

# Game variables
score = 0
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

# Function to reset game variables
def reset_game():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, paddle_x, score
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_speed_x = random.choice([-4, 4])  # Start ball moving in a random x direction
    ball_speed_y = 4  # Ball always starts by moving downwards
    paddle_x = WIDTH // 2 - paddle_width // 2
    score = 0

# Initialize game variables
reset_game()

# Main loop
running = True
while running:
    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # Get keys pressed for paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x + paddle_width < WIDTH:
            paddle_x += paddle_speed

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with screen edges
        if ball_x - radius <= 0 or ball_x + radius >= WIDTH:
            ball_speed_x *= -1  # Reverse x direction
        if ball_y - radius <= 0:
            ball_speed_y *= -1  # Reverse y direction on top collision

        # Ball collision with the paddle
        if (paddle_y <= ball_y + radius <= paddle_y + paddle_height and
            paddle_x <= ball_x <= paddle_x + paddle_width):
            ball_speed_y *= -1  # Bounce the ball up
            score += 1  # Increase score on each successful bounce

        # Check if the ball falls below the paddle (Game Over)
        if ball_y + radius >= HEIGHT:
            break  # Exit the main game loop to show Game Over screen

        # Clear screen
        window.fill(LIGHT_BLUE)

        # Draw the paddle
        pygame.draw.rect(window, BLACK, (paddle_x, paddle_y, paddle_width, paddle_height))

        # Draw the ball
        pygame.draw.circle(window, RED, (ball_x, ball_y), radius)

        # Draw the score
        score_text = font.render(f"Score: {score}", True, BLACK)
        window.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Control the frame rate
        time.sleep(0.01)

    # Game Over screen with reset option
    window.fill(LIGHT_BLUE)
    game_over_text = game_over_font.render("GAME OVER", True, RED)
    reset_text = font.render("Press 'R' to Restart or 'Q' to Quit", True, BLACK)
    window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    window.blit(reset_text, (WIDTH // 2 - reset_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()

    # Wait for player input to reset or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset game
                    reset_game()
                    break
                elif event.key == pygame.K_q:  # Quit game
                    running = False
                    break
        if ball_y + radius < HEIGHT or not running:
            break

# Quit Pygame
pygame.quit()
