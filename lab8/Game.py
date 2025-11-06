#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab8\AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab8\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab8\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    def collect_coin(self, coins):
        collisions = pygame.sprite.spritecollide(self, coins, True)
        for coin in collisions:
            return True
        return False
                  
class Coin(pygame.sprite.Sprite):   # Define Coin as a sprite (inherits from pygame's Sprite)
    def __init__(self):     # Constructor — runs when a Coin object is created
        super().__init__()      # Initialize parent Sprite class
        self.image = pygame.image.load(r"C:\Users\zibek\Documents\Codes\pp2\lab8\Coin.png")
        self.rect = self.image.get_rect()       # Get rectangle (position & size) for the image
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)       # Set initial position: random X, Y = 0 (top)

    def move(self):
        self.rect.move_ip(0, SPEED)     # Move the coin downward by SPEED pixels
        if self.rect.top > 600:     # If the coin goes below the screen
            self.rect.top = 0       # Reset it to the top
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)       # Give it a new random X position

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0, 0))        # Draw the background image at the top-left corner of the screen
    scores = font_small.render(str(SCORE), True, BLACK)      # Render the current score as black text
    coin_scores = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)    # Render the coin count as black text with label
    DISPLAYSURF.blit(scores, (10, 10))      # Draw (blit) the score text near the top-left corner
    DISPLAYSURF.blit(coin_scores, (300, 10))    # Draw the coin score text near the top-right corner

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    if P1.collect_coin(coins):
        COIN_SCORE += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r"C:\Users\zibek\Documents\Codes\pp2\lab8\crash.wav").play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
