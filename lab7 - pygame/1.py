'''
pygame.draw.line(screen, color, (x0, y0), (x1, y1), width)
pygame.draw.lines(screen, color, bool, [(x0, y0), (x1, y1), (x2, x2), ..., (xn, yn)], width)

pygame.draw.polygon(surface, color, [points], width=0)              - [points] - points connected in series
pygame.draw.rect(screen, color, (x0, y0, width, height), border)

pygame.draw.circle(screen, color, (x, y), R, border)
pygame.draw.ellipse(screen, color, [x0, y0, width, height], width)
pygame.draw.arc(screen, color, [x0, y0, width, height], start_angle, end_angle, width)

'''

import pygame
from datetime import datetime

pygame.init()

base = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab7 - pygame\base.jpg")
left_hand = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab7 - pygame\minute.png")
right_hand = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab7 - pygame\second.png")
hour_hand = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab7 - pygame\second.png")

screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()

mainclock_rect = base.get_rect(center=(450, 450))
left_hand_rect = left_hand.get_rect(center=mainclock_rect.center)
right_hand_rect = right_hand.get_rect(center=mainclock_rect.center)
hour_hand_rect = hour_hand.get_rect(center=mainclock_rect.center)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.now().time()

    second_angle = current_time.second * 6
    minutes_angle = current_time.minute * 6 + current_time.second * 0.1
    hour_angle = current_time.hour * 30 + current_time.minute / 2

    rt_left_hand = pygame.transform.rotate(left_hand, -second_angle)
    rt_right_hand = pygame.transform.rotate(right_hand, -minutes_angle)
    rt_hour_hand = pygame.transform.rotate(hour_hand, -hour_angle)

    left_hand_rect = rt_left_hand.get_rect(center=mainclock_rect.center)
    right_hand_rect = rt_right_hand.get_rect(center=mainclock_rect.center)
    hour_hand_rect = rt_hour_hand.get_rect(center=mainclock_rect.center)

    screen.blit(base, mainclock_rect)  
    screen.blit(rt_left_hand, left_hand_rect) 
    screen.blit(rt_right_hand, right_hand_rect) # "накладывает"
    screen.blit(rt_hour_hand, hour_hand_rect)

    pygame.display.update([left_hand_rect, right_hand_rect, hour_hand_rect])

    clock.tick(60)