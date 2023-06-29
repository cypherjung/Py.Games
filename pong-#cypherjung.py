#pong
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong-#cypherjung")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle dimensions
paddle_width, paddle_height = 10, 60

# Paddle A
paddle_a_x, paddle_a_y = 50, window_height // 2 - paddle_height // 2
paddle_a_dy = 0

# Paddle B
paddle_b_x, paddle_b_y = window_width - paddle_width - 50, window_height // 2 - paddle_height // 2
paddle_b_dy = 0

# Ball
ball_x, ball_y = window_width // 2, window_height // 2
ball_radius = 10
ball_dx = 3 * random.choice([-1, 1])
ball_dy = 3 * random.choice([-1, 1])

# Score
score_a = 0
score_b = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
game_duration = 60  # Game duration in seconds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Paddle controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_a_dy = -3
            elif event.key == pygame.K_s:
                paddle_a_dy = 3
            elif event.key == pygame.K_UP:
                paddle_b_dy = -3
            elif event.key == pygame.K_DOWN:
                paddle_b_dy = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle_a_dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_b_dy = 0

    # Update paddle positions
    paddle_a_y += paddle_a_dy
    paddle_b_y += paddle_b_dy

    # Ensure paddles stay within the window
    paddle_a_y = max(0, min(paddle_a_y, window_height - paddle_height))
    paddle_b_y = max(0, min(paddle_b_y, window_height - paddle_height))

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with paddles
    if (
        paddle_a_x + paddle_width >= ball_x >= paddle_a_x
        and paddle_a_y + paddle_height >= ball_y >= paddle_a_y
    ):
        ball_dx = abs(ball_dx)
        score_a += 1
    elif (
        paddle_b_x <= ball_x <= paddle_b_x + paddle_width
        and paddle_b_y <= ball_y <= paddle_b_y + paddle_height
    ):
        ball_dx = -abs(ball_dx)
        score_b += 1

    # Check for collisions with walls
    if ball_y + ball_radius >= window_height or ball_y - ball_radius <= 0:
        ball_dy = -ball_dy

    # Check for out-of-bounds (scoring)
    if ball_x + ball_radius >= window_width:
        score_a += 1
        ball_x, ball_y = window_width // 2, window_height // 2
        ball_dx = 3 * random.choice([-1, 1])
        ball_dy = 3 * random.choice([-1, 1])
    elif ball_x - ball_radius <= 0:
        score_b += 1
        ball_x, ball_y = window_width // 2, window_height // 2
        ball_dx = 3 * random.choice([-1, 1])
        ball_dy = 3 * random.choice([-1, 1])

    # Clear the window
    window.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(window, WHITE, (paddle_a_x, paddle_a_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (paddle_b_x, paddle_b_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)

    # Draw scores
    score_text = font.render(f"Score A: {score_a}   Score B: {score_b}", True, WHITE)
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 10))

    # Draw timer
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_left = max(game_duration - elapsed_time, 0)
    timer_text = font.render(f"Time: {time_left}", True, WHITE)
    window.blit(timer_text, (window_width // 2 - timer_text.get_width() // 2, 40))

    # Update the display
    pygame.display.flip()

    # Check for game over
    if elapsed_time >= game_duration:
        running = False

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
print("Thank you for playing")
