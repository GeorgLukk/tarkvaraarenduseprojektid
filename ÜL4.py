import pygame
import random
import sys


pygame.init()
#ekraani seaded ja skoor
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("m2ng")
clock = pygame.time.Clock()
score = 0


#piltide lisamine
tee = pygame.image.load("img/tee.jpg")
tee = pygame.transform.scale(tee, [640, 480])
tee_korX = 0
s_auto = pygame.image.load("img/sauto.png")
s_auto2 = pygame.image.load("img/sauto.png")
p_auto = pygame.image.load("img/pauto.png")


s_kiirus = 3  #sinise kiirus
p_kiirus = 0  #punase kiirus
#siniste Y koordinaadid
s_korY = random.randint(0, 100)
s2_korY = random.randint(0, 100)
#siniste X koordinaadid
s_korX = random.randint(300, 460)
s2_korX = random.randint(130, 460)
p_korX, p_korY = 300, 390  #punase koordinaadid

gameover = False
while not gameover:  #on selles loopis niikaua kui m'ng ei ole l'bi
    clock.tick(120)  # FPS
#anka sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # taustapildi lisamine
    screen.blit(tee, (0, 0))

    #siniste lisamine (pilt(kooridnaat1,kooridanaat2))
    screen.blit(s_auto, (s_korX, s_korY))
    screen.blit(s_auto2, (s2_korX, s2_korY))

    #siniste autode liigutamine ning + nendele kiirustele et see liiguks erinevatel kiirustel
    s_korY += s_kiirus + 0.6
    s2_korY += s_kiirus + 1

    # punase auto lisamine
    screen.blit(p_auto, (p_korX, p_korY))
    p_korY += p_kiirus  # auto liigutamine

    # skoori kuvamine
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {score}", True, [255, 255, 255]), [10, 20])

    # autode positsiooni taastamine
    #kui sinised autod jõuavad alla siis viiakse need ülesse tagasi
    if s_korY >= 480:
        s_korY = -120
        score += 1
        s_korX = random.randint(130, 280)

    if s2_korY >= 480:
        s2_korY = -120
        score += 1
        s2_korX = random.randint(300, 480)

    if p_korY >= 480:
        p_korY = -120

    # punase auto liigutamine noole nuppudega
    key = pygame.key.get_pressed()  # kui vajutatakse klahvi
    if key[pygame.K_LEFT]:  # vasakut
        p_korX -= 5  # liigutame autot vasakule
    if key[pygame.K_RIGHT]:  #paremat
        p_korX += 5  # liigutame autot paremale

    # mängu lõpp, kui sinine auto puudutab punast
    if p_korY + 55 >= s_korY >= p_korY - 55:  # kui sinine ja punane auto on samal Y kordinaadil
        if p_korX + 50 >= s_korX >= p_korX - 50:  # kui sinine ja punane auto on ka samal X kordinaadil
            gameover = True #mäng saab läbi

    if p_korY + 55 >= s2_korY >= p_korY - 55:  #kui teine sinine ja punane auto on samal Y kordinaadil
        if p_korX + 50 >= s2_korX >= p_korX - 50:  #kui teine sinine ja punane auto on ka samal X kordinaadil
            gameover = True #mäng saab läbi

    pygame.display.flip()  # värksendab ekraani
while True:
    if gameover:  # kui mäng on läbi
            # prindime ekraanile "Game over"
        screen.blit(pygame.font.Font(None, 50).render("Game over!", True, [255, 255, 255]), [230, 300])
            # prindime ekraanile Sinu skoor (ning saadud skoor)
        screen.blit(pygame.font.Font(None, 50).render(f"Skoor: {score}", True, [255, 255, 255]),
                    [240, 200])
        pygame.display.flip()  # värksendab ekraani
    for event in pygame.event.get():  # ootame sündmust
        if event.type == pygame.QUIT:  # kui ekraan suletakse
            sys.exit()  # lõpetame mängu