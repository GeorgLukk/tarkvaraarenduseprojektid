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

# palli ja puulaua piltide ja suuruste lisamine
ball = pygame.image.load("img/ball.png")
ball = pygame.transform.scale(ball, [20,20])
pad = pygame.image.load("img/pad.png")
pad = pygame.transform.scale(pad, [120,20])
# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3
pposX = 320
pposY = 400



a=1
#alustab mängu tsükli ning lisab selle sisse mängu komponendid
#kuna selles mängus polnud gameoverit siis
while a<3:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))
    screen.blit(pad, (pposX, pposY))

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
    if posX > pposX - ball.get_rect().width or pposX < 0:
        speedX = -speedX
        # kui palli positsioon on suurem kui screenX siis see läheb kuhugi muusse suunda
    if posY > pposY - ball.get_rect().height or pposY < 0:
        speedY = -speedY

    pygame.display.flip()#värskendab ekraani
    screen.fill(black)#täidab tausta valitud värviga

pygame.quit()