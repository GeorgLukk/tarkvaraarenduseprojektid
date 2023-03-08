import pygame, sys
from pygame import mixer
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
#lisa helid ning taust
pygame.mixer.music.load('cave themeb4.ogg')
hit = pygame.mixer.Sound('hit.wav')
pygame.mixer.Sound.set_volume(hit,0.2)
pygame.mixer.music.play(-1)
taust = pygame.image.load("obrin-7.png")
taust = pygame.transform.scale(taust, [640, 640])


# kiirus ja asukoht
posX, posY = 0, 0       #palli algne positsioon
ballspeed = 3
speedX, speedY = 3, 4   #palli x ja y kiirused
aspeedX, aspeedY = 3,0  #palgi x ja y kiirused
pposX = 300             #palgi algne X positsioon
pposY = screenY/1.2     #palgi algne Y positsioon

# palli ja puulaua piltide ja suuruste lisamine
#piltide laadimine
ball = pygame.image.load("ball.png")
pad = pygame.image.load("pad.png")
#piltide suuruste määramine
ball = pygame.transform.scale(ball, [20,20])
pad = pygame.transform.scale(pad, [120,20])
#pallile ja palgile ristküliku tegemine
ball_rect = pygame.Rect(posX,posY,20,20)
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
    screen.blit(taust, [0, 0])
    screen.blit(ball, (posX, posY))
    screen.blit(pad, (pposX, pposY))
    #pallile ja palgile ristküliku tegemine
    pall = pygame.Rect(posX,posY,20,20)
    pad_rect = pygame.Rect(pposX, pposY, 120, 20)

    #palli liikuma panemine
    posX += speedX
    posY += speedY

    #palgi liigutamine
    key = pygame.key.get_pressed()  # kui vajutatakse klahvi
    if key[pygame.K_LEFT]:      # vasakut
        pposX -= 5              # liigutame palki vasakule
    if key[pygame.K_RIGHT]:     # paremat
        pposX += 5              # liigutame palki paremale

    #Score kuvamine
    screen.blit(pygame.font.Font(None, 30).render(f"Score: {score}", True, [255, 255, 255]),
                [10, 20])       # skoori kuvamine
    # kui puudub ääri, siis muudab suunda
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX #teeb kiirusest negatiivse kiiruse
    #kui palli positsioon on suurem kui screenX siis see läheb kuhugi muusse suunda
    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
    #kui pall läheb palgist mööda siis lõppeb mäng
    if posY > screenY -ball.get_rect().height:
        gameover = True         #lõpetab selle tsükli ehk lõpetab mängu
    # kui palk tahab minna alast välja siis see eemaldub äärest
    if pposX > screenX - pad.get_rect().width or pposX < 0:
        pposX = -pposX

    # kui pall puutub palki siis see põrkab ning lisab skoori
    if pall.colliderect(pad_rect) and speedY > 0:
        speedY = -speedY
        score +=1
        pygame.mixer.Sound.play(hit)

    pygame.display.flip()   #värskendab ekraani
    screen.fill(lGreen)     #täidab tausta valitud värviga

pygame.quit()