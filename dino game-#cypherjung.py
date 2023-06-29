#dino game
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game-#cypherjung")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the ground
ground = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)

# Set up the player
player_width, player_height = 50, 50
player = pygame.Rect(50, HEIGHT - player_height - ground.height, player_width, player_height)
player_color = (255, 0, 0)

# Set up cacti
cactus_width, cactus_height = 20, 50
cactus_gap = 200
cactus_color = (0, 255, 0)
cacti = []
cactus_spawn_time = pygame.USEREVENT + 1
pygame.time.set_timer(cactus_spawn_time, 1200)

# Set up variables
clock = pygame.time.Clock()
score = 0
is_jumping = False
jump_count = 10

# Load font
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jump_count = 10

        elif event.type == cactus_spawn_time:
            cactus_height = random.randint(50, 100)
            cactus = pygame.Rect(WIDTH, HEIGHT - cactus_height - ground.height, cactus_width, cactus_height)
            cacti.append(cactus)

    # Jumping logic
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False

    # Update player position
    player.y += 5

    # Collision detection
    if player.colliderect(ground):
        is_jumping = False
        player.y = HEIGHT - player_height - ground.height

    for cactus in cacti:
        cactus.x -= 5
        if cactus.colliderect(player):
            running = False
        if cactus.x + cactus.width < 0:
            cacti.remove(cactus)
            score += 1

    # Draw everything on the screen
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK, ground)
    pygame.draw.rect(window, player_color, player)
    for cactus in cacti:
        pygame.draw.rect(window, cactus_color, cactus)

    # Display score
    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (10, 10))

    # Update the window
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()

