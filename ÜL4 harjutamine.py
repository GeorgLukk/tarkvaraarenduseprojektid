#PALLI ANIMEERIMINE
'''
import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)

# graafika laadimine
ball = pygame.image.load("img/ball.png")

# kiirus ja asukoht
posX, posY = 0, 0

gameover = False
while not gameover:
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    # graafika kuvamine ekraanil
    pygame.display.flip()

pygame.quit()
'''
'''
import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)

# graafika laadimine
ball = pygame.image.load("img/ball.png")

# kiirus ja asukoht
posX, posY = 0, 0
speedX = 1

gameover = False
while not gameover:
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    posX += speedX

    # graafika kuvamine ekraanil
    pygame.display.flip()

pygame.quit()
'''
'''
import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
white = [255,255,255]
black = [0,0,0]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(black)
clock = pygame.time.Clock()

# pildi laadimine seal kuhu lisasite selle
ball = pygame.image.load("img/ball.png")

# kiirus ja asukoht
posX, posY = 0, 0
speedX = 3

gameover = False
#alustab mängu tsükli ning lisab selle sisse mängu komponendid
while not gameover:
    # fps(frames per second)
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    posX += speedX

    # graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(black)

pygame.quit()
'''
'''
import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
white = [255,255,255]
black = [0,0,0]


# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(black)
clock = pygame.time.Clock()

# graafika laadimine
ball = pygame.image.load("img/ball.png")

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4

gameover = False
#alustab mängu tsükli ning lisab selle sisse mängu komponendid
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    posX += speedX
    posY += speedY

    # kui puudub ääri, siis muudab suunda
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX
#kui palli positsioon on suurem kui screenX siis see läheb kuhugi muusse suunda
    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
# kui palli positsioon on suurem kui screenY siis see läheb kuhugi muusse suunda
    # graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(black)

pygame.quit()
'''
#RUUTUDE ANIMEERIMINE

import pygame, sys, random

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
#ise lisatud 2 värvi
white = [255,255,255]
black = [0,0,0]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(black)
clock = pygame.time.Clock()
#

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3


# koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(10):
    posX = random.randint(1, screenX)#koordinaat 1
    posY = random.randint(1, screenY)#koordinaat 2
    speed = random.randint(1,5)#lisab kiiruse mis on suvaline 1'st 5'ni
    coords.append([posX, posY, speed])

gameover = False
#alustab mängu tsükli ning lisab selle sisse mängu komponendid
while not gameover:
    # fps
    clock.tick(120)
    # mängu sulgemine ristist(mis ei toimi)
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # loendist koordinaadid
    for i in range(len(coords)):
        pygame.draw.rect(screen, white, [coords[i][0], coords[i][1], 20, 20])
        coords[i][1] += coords[i][2]
        # kui jõuab alla, siis muudame ruudu alguspunkti
        if coords[i][1] > screenY:#kui ruudu koordinaat on suurem kui screenY siis see teeb järgmisi asju
            coords[i][1] = random.randint(-40, -10)#annab ruudule uue asukoha
            coords[i][0] = random.randint(0, screenX)

    pygame.display.flip()
    screen.fill(black)
pygame.quit()

