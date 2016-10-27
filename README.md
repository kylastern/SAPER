# SAPER
# :D
class Saper:
    idz
    rozbroj
    przewiez
    desant
# kratka #
import pygame, sys
from pygame.locals import *
  
pygame.init()
  

mapa = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Drawing')
  

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
  

mapa.fill(WHITE)
wysokosc=600
szerokosc=800
kratka=50

for x in range(0, szerokosc, kratka): # linie pionowe
        pygame.draw.line(mapa, BLACK, (x, 0), (x, wysokosc))
for y in range(0, wysokosc, kratka): # linie poziome
        pygame.draw.line(mapa, BLACK, (0, y), (szerokosc, y)) 

  

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
    
    
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    
    import pygame, sys
from pygame import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Paddle Movement')


PADDLE_WIDTH = 50
PADDLE_HEIGHT = 10
paddleSpeedX = 0
p1Paddle = pygame.Rect(10, 430, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_COLOR = pygame.color.Color("red")

# clock object that will be used to make the game
# have the same speed on all machines regardless
# of the actual machine speed.
clock = pygame.time.Clock()

while True:
    # limit the demo to 50 frames per second
    clock.tick( 50 );

    # clear screen with black color
    screen.fill( (0,0,0) )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        p1Paddle.left = p1Paddle.left + paddleSpeedX - 5

    if keys[K_RIGHT]:
        p1Paddle.left = p1Paddle.left + paddleSpeedX + 5

    if keys[K_] 

    # draw the paddle
    screen.fill( PADDLE_COLOR, p1Paddle );

    pygame.display.update()

  
