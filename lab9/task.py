'''
import pygame
import time
import random
import sys

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
speed = 20
clock = pygame.time.Clock()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Rectangle")


running = True

def generate_triangle(screen, p1,p2, color,w, rect): #Generate food in a random cell that is not on the snake
    while True:
        x1 = random.randrange(0, w, 20)
        x2 = random.randrange(0, w, 20)
        y1 = random.randrange(0, h, 20)
        y2 = random.randrange(0, h, 20)

        x1, y1 = p1
        x2, y2 = p2
        points = [(x1, y1), (x2, y1), (x1, y2)]
        trian = pygame.draw.polygon(screen, GREEN, points, w)
        if (p1, p2) not in rect:
            return {
                "p1": p1,
                "p2": p2,
                "spawn_time": time.time()  
            }
        
def changing_color(food, lifetime=2):
    if time.time() - food["spawn_time"] >= lifetime:
        return True # return True if food expired
    return False
        
while running:
    screen.fill((255, 255, 255))
    rect = pygame.draw.rect(screen, BLACK, (250, 250), 20)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(y - speed, 20)
            elif event.key == pygame.K_DOWN:
                y = min(y + speed, h - 20)
            elif event.key == pygame.K_LEFT:
                x = max(x - speed, 20)
            elif event.key == pygame.K_RIGHT:
                x = min(x + speed, w - 20)

    if rect == trian:
        '''