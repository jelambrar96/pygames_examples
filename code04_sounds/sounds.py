import pygame
import time, sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Hello World')

soundObj = pygame.mixer.Sound("beeps.wav")
soundObj.play()
time.sleep(1)
soundObj.stop()


