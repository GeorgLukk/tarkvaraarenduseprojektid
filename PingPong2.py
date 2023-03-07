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
pygame.display.set_caption("Ping-pong")
screen.fill(black)
clock = pygame.time.Clock()
score = 0
l6pp = "Kaotasid"

# kiirus ja asukoht
posX, posY = 0, 0       #palli algne positsioon
speedX, speedY = 3, 4   #palli x ja y kiirused
aspeedX, aspeedY = 3,0  #palgi x ja y kiirused
pposX = 300   #palgi algne positsioon
pposY = screenY/1.2

# palli ja puulaua piltide ja suuruste lisamine
ball = pygame.image.load("img/ball.png")
ball = pygame.transform.scale(ball, [20,20])
ball_rect = pygame.Rect(posX,posY,20,20)
pad = pygame.image.load("img/pad.png")
pad = pygame.transform.scale(pad, [120,20])
pad_rect = pygame.Rect(pposX,pposY,120,20)

#helid
#puute_heli=

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
    screen.blit(pad, (pposX, pposY))
    pall = pygame.Rect(posX,posY,20,20)
    pad_rect = pygame.Rect(pposX, pposY, 120, 20)

    #palli liikuma panemine
    posX += speedX
    posY += speedY



    #palgi liigutamine
    key = pygame.key.get_pressed()  # kui vajutatakse klahvi
    if key[pygame.K_LEFT]:  # vasakut
        pposX -= 5  # liigutame palki vasakule
    if key[pygame.K_RIGHT]:  # paremat
        pposX += 5  # liigutame palki paremale

    #Score
    screen.blit(pygame.font.Font(None, 30).render(f"Score: {score}", True, [255, 255, 255]),
                [10, 20])  # skoori kuvamine
    # kui puudub ääri, siis muudab suunda
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX #teeb kiirusest negatiivse kiiruse
    #kui palli positsioon on suurem kui screenX siis see läheb kuhugi muusse suunda
    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
    #kui pall läheb palgist mööda siis läheb punkt skoorist maha
    if posY > screenY -ball.get_rect().height:
        gameover = True
    # kui palgi positsioon on suurem
    if pposX > screenX - pad.get_rect().width or pposX < 0:
        pposX = -pposX

    # kui pall puutub palki siis see põrkab ning lisab skoori
    if pall.colliderect(pad_rect) and speedY > 0:
        speedY = -speedY
        score +=1
    if gameover == True:
        screen.blit(pygame.font.Font(None, 30).render(f"Sa {l6pp}", True, [255, 255, 255]),
                    [10, 20])  # skoori kuvamine

    pygame.display.flip()#värskendab ekraani
    screen.fill(lGreen)#täidab tausta valitud värviga

pygame.quit()