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