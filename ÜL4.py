import pygame
import random
import sys
import time

pygame.init()

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("m2ng")
clock = pygame.time.Clock()

white = [255,255,255]

teeX,teeY = 300,300
posX,posY = 330, 330
tee_s = pygame.surface([teeX,teeY])
speedX, speedY = 3, 3
#koordinaadid
coords = []
for i in range (10):
    posX = random.randint(1,posX)
    posY = random.randint(1,posY)
    speed = random.randint(1, 3)
    coords.append([posX, posY,speed])


#piltide lisamine
tee = pygame.image.load("img/tee.jpg")
s_auto = pygame.image.load("img/sauto.png")
p_auto = pygame.image.load("img/pauto.png")
tee = pygame.transform.scale(tee, [640, 480])
s_auto = pygame.transform.scale(s_auto, [70, 100])
p_auto = pygame.transform.scale(p_auto, [70, 100])
screen.blit(tee,[0,0])



gameover = False
while not gameover:

    clock.tick(120)
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()


    for i in range(len(coords)):
        pygame.draw.rect(tee_s, white, [coords[i][0], coords[i][1], 20, 20])
        coords[i][1] += coords[i][2]
        # kui jõuab alla, siis muudame ruudu alguspunkti
        if coords[i][1] > screenY:#kui ruudu koordinaat on suurem kui screenY siis see teeb järgmisi asju
            coords[i][1] = random.randint(-40, -10)#annab ruudule uue asukoha
            coords[i][0] = random.randint(0, screenX)


pygame.display.flip()

pygame.quit()