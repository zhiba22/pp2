import pygame
import random
import sys

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


# а function to draw text on screen
def draw_text(text, color, x, y):
    surface = font.render(text, True, color) # создаем поверхность с текстом
    screen.blit(surface, (x, y)) # накладываем текст на экран


# Initialize snake and food
snake = [(100, 100), (80, 100), (60, 100)]  # Snake starts with 3 blocks
snake_dir = "RIGHT"  # Initial direction
food_pos = (300, 300)  # Starting food position
food_spawn = True

score = 0
level = 1
speed = 10  


def generate_food(): #Generate food in a random cell that is not on the snake
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake:  # Make sure food not on snake
            return (x, y)


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != "DOWN":
        snake_dir = "UP"
    if keys[pygame.K_DOWN] and snake_dir != "UP":
        snake_dir = "DOWN"
    if keys[pygame.K_LEFT] and snake_dir != "RIGHT":
        snake_dir = "LEFT"
    if keys[pygame.K_RIGHT] and snake_dir != "LEFT":
        snake_dir = "RIGHT"

    # Move the snake by adding a new head
    head_x, head_y = snake[0] # a coordinate of a head 
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

    # Check if snake hits food
    if new_head == food_pos:
        score += 1
        food_spawn = False
    else:
        snake.pop()  # Remove last segment unless eating food

    # Spawn new food
    if not food_spawn:
        food_pos = generate_food()
        food_spawn = True


    # Every 4 points → next level and faster speed
    if score != 0 and score % 4 == 0:
        level = score // 4 + 1
        speed = 10 + (level - 1) * 3  # Increase speed each level


    # If snake hits wall game over
    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):
        pygame.quit()
        sys.exit()

    # If snake hits itself game over
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)


    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))


    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Draw score and level
    draw_text(f"Score: {score}", WHITE, 10, 10)
    draw_text(f"Level: {level}", WHITE, 480, 10)

    pygame.display.update()

    clock.tick(speed)
