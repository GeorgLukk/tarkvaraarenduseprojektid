import pygame
pygame.init()
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")


#piltide lisamine
tee = pygame.image.load("img/tee.png")
s_auto = pygame.image.load("img/sauto.png")
p_auto = pygame.image.load("img/pauto.png")
screen.fill(tee)