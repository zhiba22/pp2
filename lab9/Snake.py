import pygame
import random
import sys
import time

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 24)

clock = pygame.time.Clock()


# Draw text
def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


FOOD_WEIGHTS = {
    1: 0.6,  # 60% chance  RED
    2: 0.3,  # 30% chance  BLUE
    5: 0.1   # 10% chance  WHITE
    }


def choose_weight():
    return random.choices(list(FOOD_WEIGHTS.keys()), list(FOOD_WEIGHTS.values()))[0]


def generate_food(snake):
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake:
            return {
                "x": x,
                "y": y,
                "weight": choose_weight(),
                "spawn_time": time.time()  # needed for expiration
            }


def remove_expired_food(food, lifetime=5):
    if time.time() - food["spawn_time"] >= lifetime:
        return True # return True if food expired
    return False


snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = "RIGHT"

food = generate_food(snake)   # food is now an object with weight + timer

score = 0
level = 1
speed = 10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != "DOWN":
        snake_dir = "UP"
    if keys[pygame.K_DOWN] and snake_dir != "UP":
        snake_dir = "DOWN"
    if keys[pygame.K_LEFT] and snake_dir != "RIGHT":
        snake_dir = "LEFT"
    if keys[pygame.K_RIGHT] and snake_dir != "LEFT":
        snake_dir = "RIGHT"

    # Move snake by adding new head 
    head_x, head_y = snake[0]
    if snake_dir == "UP":
        head_y -= CELL_SIZE
    elif snake_dir == "DOWN":
        head_y += CELL_SIZE
    elif snake_dir == "LEFT":
        head_x -= CELL_SIZE
    elif snake_dir == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    # Eating food?
    if new_head == (food["x"], food["y"]):
        score += food["weight"]  # weighted scoring
        food = generate_food(snake)  # respawn food
    else:
        snake.pop()

    if remove_expired_food(food, lifetime=5): # expired food 
        food = generate_food(snake)

    # Level-up logic
    if score != 0 and score % 4 == 0:
        level = score // 4 + 1
        speed = 10 + (level - 1) * 1.5

    # Wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Self collision
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()

    # Drawing
    screen.fill(BLACK)

    # Draw snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL_SIZE, CELL_SIZE))

    # Draw food (color depends on weight)
    food_color = RED if food["weight"] == 1 else BLUE if food["weight"] == 2 else WHITE
    pygame.draw.rect(screen, food_color, (food["x"], food["y"], CELL_SIZE, CELL_SIZE))

    # Draw UI
    draw_text(f"Score: {score}", WHITE, 10, 10)
    draw_text(f"Level: {level}", WHITE, 480, 10)

    pygame.display.update()
    clock.tick(speed)
