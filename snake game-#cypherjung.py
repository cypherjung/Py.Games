#snake game
import pygame
import random

# Window dimensions
WIDTH = 600
HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 10

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game-#cypherjung")

clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = SNAKE_SIZE
        self.dy = 0
        self.body = [(self.x, self.y)]
        self.length = 1

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    def move(self):
        self.x += self.dx
        self.y += self.dy

        self.body.append((self.x, self.y))

        if len(self.body) > self.length:
            del self.body[0]

    def check_collision(self):
        if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
            return True

        for segment in self.body[:-1]:
            if segment == (self.x, self.y):
                return True

        return False

    def change_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

# Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        self.y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, SNAKE_SIZE, SNAKE_SIZE))

# Game loop
def game_loop():
    snake = Snake()
    food = Food()
    score = 0
    level = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.dx != SNAKE_SIZE:
                    snake.change_direction(-SNAKE_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.dx != -SNAKE_SIZE:
                    snake.change_direction(SNAKE_SIZE, 0)
                elif event.key == pygame.K_UP and snake.dy != SNAKE_SIZE:
                    snake.change_direction(0, -SNAKE_SIZE)
                elif event.key == pygame.K_DOWN and snake.dy != -SNAKE_SIZE:
                    snake.change_direction(0, SNAKE_SIZE)

        snake.move()

        if snake.check_collision():
            pygame.quit()
            quit()

        if snake.x == food.x and snake.y == food.y:
            snake.length += 1
            score += 1
            if score % 5 == 0:
                level += 1
            food = Food()

        window.fill(BLACK)
        snake.draw()
        food.draw()
        pygame.display.update()

        clock.tick(SNAKE_SPEED + level)

game_loop()

