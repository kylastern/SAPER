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
    
    # co to? #
    
import pygame, sys, time, random
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Paint")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

windowSurface.fill(WHITE)

info = pygame.display.Info()
sw = info.current_w
sh = info.current_h

x = y = 0

dx = 5
dy = 2


while True:
    windowSurface.fill(WHITE) #This clears the screen on each redraw
    pygame.draw.polygon(windowSurface,BLUE,((0+x,250+y),(120+x,120+y),(55+x,55+y)))
    pygame.draw.polygon(windowSurface,RED,((0+x,150+y),(85+x,85+y),(100+x,175+y),(0+x,150+y)))
    pygame.draw.line(windowSurface,BLACK,(60+x,85+y), (120+x, 110+y), 6)
    pygame.draw.circle(windowSurface, GREEN , (75+x,100+y), 13, 0)

    x += dx
    y += dy

    if x < 0 or x > sw-120:
    dx = -dx
    x += dx
if y < -85 or y > sh-175:
    dy = -dy
    y += dy 

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

