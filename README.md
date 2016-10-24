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
