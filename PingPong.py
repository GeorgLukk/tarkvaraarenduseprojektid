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
pposX = 320
pposY = 400

pad = pygame.Rect(pposX, pposY, 120, 20)
padpilt = pygame.image.load("img/pad.png")
padpilt = pygame.transform.scale(padpilt, [pad.width, pad.height])


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
    screen.blit(padpilt, (pposX, pposY))

    posX += speedX
    posY += speedY

    key = pygame.key.get_pressed()  # kui vajutatakse klahvi
    if key[pygame.K_LEFT]:  # vasakut
        pposX -= 5  # liigutame autot vasakule
    if key[pygame.K_RIGHT]:  # paremat
        pposX += 5  # liigutame autot paremale



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