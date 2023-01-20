'''
#lisa 1
#alustab koodi ja impordib selle mooduli
import pygame
pygame.init()
#teeb akna
screen=pygame.display.set_mode([300,500])
pygame.display.set_caption("lumememm - Georg")#annab aknale nime
#kujundite joonistamine
pygame.draw.rect(screen, [222, 222, 222], [90, 10, 130, 270], 2)#joonistab ristküliku
pygame.draw.circle(screen, [0, 255, 11], [155,60], 40, 0)#joonistab esimese ringi ja täidab selle värviga
pygame.draw.circle(screen, [255, 246, 0], [155,145], 40, 0)#joonistab teise ringi ja täidab selle värviga
pygame.draw.circle(screen, [255, 45, 0], [155,230], 40, 0)#joonistab kolmanda ringi ja täidab selle värviga
pygame.draw.line(screen, [222,222,222], [155,280], [155,390], 2) #teeb posti
#hakkab seda alust joonistama
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
            running == False
'''
'''
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
            running == False
'''
'''
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
            running == False
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
            running == False
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
screen.blit(tort,[480,180])
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
