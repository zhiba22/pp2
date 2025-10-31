import pygame 

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Circle movement")

radius = 25
speed = 20

x, y = w//2, h//2

while True:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(y - speed, radius)
            elif event.key == pygame.K_DOWN:
                y = min(y + speed, h - radius)
            elif event.key == pygame.K_LEFT:
                x = max(x - speed, radius)
            elif event.key == pygame.K_RIGHT:
                x = min(x + speed, w - radius)


        '''
if event.key == pygame.K_UP:
    if y - speed >= radius:  
        y -= speed

elif event.key == pygame.K_DOWN:
    if y + speed <= h - radius:  
        y += speed

elif event.key == pygame.K_LEFT:
    if x - speed >= radius:   
        x -= speed

elif event.key == pygame.K_RIGHT:
    if x + speed <= w - radius:  
        x += speed
'''