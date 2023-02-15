'''
#lisa 1
#alustab koodi ja impordib selle mooduli
import pygame
pygame.init()
#teeb akna
screen=pygame.display.set_mode([300,500])
pygame.display.set_caption("Valgusfoor- Georg")#annab aknale nime
#kujundite joonistamine
pygame.draw.rect(screen, [222, 222, 222], [90, 10, 130, 270], 2)#joonistab ristküliku
pygame.draw.circle(screen, [0, 255, 11], [155,60], 40, 0)#joonistab esimese ringi ja täidab selle värviga
#pygame.draw.circle(screen, 1.([0, 255, 11]), 2.([155,60]), 3.(40), 4.(0))=1.[Värvi rgb kood] 2.[koordinaadid] 3.ringi raadius 4.0 on seest täitmine, 2 on tühi
pygame.draw.circle(screen, [255, 246, 0], [155,145], 40, 0)#joonistab teise ringi ja täidab selle värviga
pygame.draw.circle(screen, [255, 45, 0], [155,230], 40, 0)#joonistab kolmanda ringi ja täidab selle värviga
pygame.draw.line(screen, [222,222,222], [155,280], [155,390], 2) #teeb posti
#hakkab seda alust joonistama
#pygame.draw.polygon(screen, [värv], [[koordinaadid 1],[koordinaadid 2],[koordinaadid 3],[koordinaadid 4],[koordinaadid 5]], 2)
pygame.draw.polygon(screen, [126, 128, 130], [[100,390],[190,390],[250,450],[40,450],[100,390]], 2)
pygame.draw.polygon(screen, [0, 123, 255], [[130,390],[190,390],[210,410],[80,410],[100,390]], 0)
pygame.draw.polygon(screen, [3, 3, 3], [[80,410],[210,410],[230,430],[60,430],[80,410]], 0)
pygame.draw.polygon(screen, [255, 255, 255], [[60,430],[230,430],[250,450],[40,450],[60,430]], 0)
pygame.display.flip()#värskendab akna
#hoiab akna lahti
running = True
while running:#teeb tsükli
    for event in pygame.event.get():#kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT:#kui programm pannakse kinni läheb ka pygame kinni
            running = False
pygame.quit()
'''
'''
#harjutamine
#tekstide ja piltide kasutamine
import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])#annab resulutsiooni loodud aknale
pygame.display.set_caption("Harjutamine")#annab aknale nime
screen.fill([204, 255, 204])#paneb taustavärvi
#lisame teksti
#font = pygame.font.SysFont("Tahoma", 50)
font = pygame.font.Font(pygame.font.match_font('arial'), 50)
font = pygame.font.Font(None, 30)#annab testile fondi ning selle suuruse
text = font.render("Hello PyGame", True, [0,0,0])#kirjutab selle lause ning annab selle värvi
screen.blit(text, [220,220])#vaatab mis koodrinaatidele on see tekst kirjutatud
pygame.display.flip()#värskendab lehte
#hoiab akna lahti
running = True
while running:#teeb tsükli
    for event in pygame.event.get():#kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT:#kui programm pannakse kinni läheb ka pygame kinni
            running = False
pygame.quit()
'''
'''
#Harjutamine
import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])#annab resulutsiooni loodud aknale
pygame.display.set_caption("Harjutamine")#annab aknale nime
screen.fill([204, 255, 204])#paneb taustavärvi
#lisame teksti
font = pygame.font.Font(pygame.font.match_font('arial'), 50)#annab tekstile uue fondi
font.set_underline(True)#lisab alumise joone
text = font.render("Hello PyGame", True, [0,0,0])#kirjutab selle lause ja vaatab mis see värv on
#tekstikasti suurus
text_width = text.get_rect().width#annab tekstikastile laiuse
text_height = text.get_rect().height#annab tekstikastile laiuse
screen.blit(text, [320-text_width/2,240-text_height/2])
pygame.display.flip()
running = True
while running:#teeb tsükli
    for event in pygame.event.get():#kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT:#kui programm pannakse kinni läheb ka pygame kinni
            running = False
pygame.quit()
'''
'''
#ülessane 2 harjutamine
import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])#annab resulutsiooni loodud aknale
pygame.display.set_caption("Harjutamine")#annab aknale nime
screen.fill([204, 255, 204])#paneb taustavärvi
#Lisame pildid
bg = pygame.image.load("img/pilt.jpg")
screen.blit(bg,[0,0])

pygame.display.flip()
running = True
while running:#teeb tsükli
    for event in pygame.event.get():#kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT:#kui programm pannakse kinni läheb ka pygame kinni
            running = False
pygame.quit()
'''
'''
#Ülessanne 2 tekstide ja piltide kasutamine
import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])#annab resulutsiooni loodud aknale
pygame.display.set_caption("Ülessanne 2")#annab aknale nime
screen.fill([204, 255, 204])#paneb taustavärvi
#Lisame pildid
#pead tegema endale directory piltide jaoks kuhu sa pildid laed
bg_shop = pygame.image.load("img/bg_shop.jpg")
seller = pygame.image.load("img/seller.png")
chat = pygame.image.load("img/chat.png")
#annme piltidele suurused
bg_shop = pygame.transform.scale(bg_shop, [640, 480])
seller = pygame.transform.scale(seller, [300, 240])
chat = pygame.transform.scale(chat, [200, 100])
#anname pilltidele asukoha koordinaadid
screen.blit(bg_shop,[0,0])
screen.blit(seller,[140,180])
screen.blit(chat,[340,150])
pygame.display.flip()#värskendab akent
font = pygame.font.Font(None, 50)#annab testile fondi ning selle suuruse
text = font.render("Georg", True, [204,20,40])#kirjutab selle lause ning annab selle värvi
screen.blit(text, [380,180])#vaatab mis koodrinaatidele on see tekst kirjutatud
pygame.display.flip()#värskendab akent
#alustab tsükli
run = True
while run: #teeb tsükli
    for event in pygame.event.get(): #kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT: #kui programm pannakse kinni läheb ka pygame kinni
            run = False
pygame.quit()
'''
'''
#Ülessanne 2 tekstide ja piltide kasutamine
import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])#annab resulutsiooni loodud aknale
pygame.display.set_caption("Ülessanne 2")#annab aknale nime
screen.fill([204, 255, 204])#paneb taustavärvi
#Lisame pildid
#pead tegema endale directory piltide jaoks kuhu sa pildid laed
bg_shop = pygame.image.load("img/bg_shop.jpg")
seller = pygame.image.load("img/seller.png")
chat = pygame.image.load("img/chat.png")
vikklogo = pygame.image.load("img/vikklogo.png")
mõõk = pygame.image.load("img/mõõk.png")
tort = pygame.image.load("img/tort.png")
#annme piltidele suurused
bg_shop = pygame.transform.scale(bg_shop, [640, 480])
seller = pygame.transform.scale(seller, [300, 240])
chat = pygame.transform.scale(chat, [200, 100])
vikklogo = pygame.transform.scale(vikklogo, [300, 50])
mõõk = pygame.transform.scale(mõõk, [100, 100])
tort = pygame.transform.scale(tort, [100, 100])
#anname pilltidele asukoha koordinaadid
screen.blit(bg_shop,[0,0])
screen.blit(seller,[140,180])
screen.blit(chat,[340,150])
screen.blit(vikklogo,[0,0])
screen.blit(mõõk,[480,180])
screen.blit(tort,[350,190])
pygame.display.flip()#värskendab akent
font = pygame.font.Font(None, 50)#annab testile fondi ning selle suuruse
text = font.render("Georg", True, [204,20,40])#kirjutab selle lause ning annab selle värvi
screen.blit(text, [380,180])#vaatab mis koodrinaatidele on see tekst kirjutatud
pygame.draw.rect(screen, [255, 255, 255], [0, 0, 300, 50], 2)#joonistab vikk logo ümber ristküliku
pygame.draw.arc(screen,[255,255,255], [240,0,80,50], -3.14/3, 1)#joonistab kaare vikklogo juurde joonistatud risküliku kõrvale
pygame.display.flip()#värskendab akent
#alustab tsükli !!!!!!!!!!!!!!!!!!!
run = True
while run: #teeb tsükli
    for event in pygame.event.get(): #kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT: #kui programm pannakse kinni läheb ka pygame kinni
            run = False
pygame.quit()
'''

'''
#Ülessanne 3 harjutused
#(1)

import pygame
import sys
pygame.init()

#värvid
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

gameover = False
#alsutab tsükli kui mäng ei ole võit siis see väljastab antud pildi
while not gameover:

    #Lisame pildid
    youWin = pygame.image.load("img/youwin.png")
    youWin = pygame.transform.scale(youWin, [300, 120])
    screen.blit(youWin,[180,100])

    pygame.display.flip()

pygame.quit()
'''
'''
#harjutamine
#funksioon mis joonistab maja
def drawHouse(x, y, width, height, screen, color):#see funksioon küsib kahte punkti,laiust,pikkust,eraldavat suurust ja värvi
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    lineThickness = 2#annab sellele joonele millega maja joonistatakse suurema laiuse
    pygame.draw.lines(screen, color, False, points, lineThickness)
'''
'''
#harjutamine
#imporsib erinevad moodulid
import pygame
import sys
import random

pygame.init()

#defineerib värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

# ekraani seaded
screen = pygame.display.set_mode([640, 480])#akna suurus
pygame.display.set_caption("Harjutamine")#akna nimi
screen.fill(lGreen)#akna sisene värv

# funktsioon mida seletasin üleval pool juba
def drawHouse(x, y, width, height, screen, color):#see funksioon küsib kahte punkti,laiust,pikkust,eraldavat suurust ja värvi
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    lineThickness = 2#annab sellele joonele millega maja joonistatakse suurema laiuse
    pygame.draw.lines(screen, color, False, points, lineThickness)

# kutsun funktsiooni välja ehk hakkan seda ülemist funksiooni kasutama (funksioon joonistab järgmisel real antud suuruste järgi)
drawHouse(100, 400, 300, 200, screen, red)

pygame.display.flip()
#alustab tsükli !!!!!!!!!!!!!!!!!!!
run = True
while run: #teeb tsükli
    for event in pygame.event.get(): #kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT: #kui programm pannakse kinni läheb ka pygame kinni
            run = False
pygame.quit()
'''
'''
import pygame
import colorsys
pygame.init()
screen = pygame.display.set_mode([640, 480])#akna suurus
pygame.display.set_caption("Random ruudud")#akna nimi
screen.fill([204, 255, 204])#paneb taustavärvi
pygame.draw.rect(screen, [222, 222, 222], [0, 0, 30, 30], 2)#joonistab ristküliku


pygame.display.flip()#värskendab akna
#alustab tsükli !!!!!!!!!!!!!!!!!!!
run = True
while run: #teeb tsükli
    for event in pygame.event.get(): #kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT: #kui programm pannakse kinni läheb ka pygame kinni
            run = False
pygame.quit()
'''
#Snake game
import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 640
dis_height = 640

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 4])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press U-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_u:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()