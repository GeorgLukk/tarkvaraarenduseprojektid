#lisa 1
#alustab koodi ja impordib selle mooduli
import pygame
pygame.init()
#teeb akna
screen=pygame.display.set_mode([300,400])
pygame.display.set_caption("lumememm - Georg")#annab aknale nime
#kujundite joonistamine
pygame.draw.rect(screen, [222, 222, 222], [90, 10, 130, 270], 2)#joonistab ristküliku
pygame.draw.circle(screen, [0, 255, 11], [155,60], 40, 0)#joonistab esimese ringi ja täidab selle värviga
pygame.draw.circle(screen, [255, 246, 0], [155,145], 40, 0)#joonistab teise ringi ja täidab selle värviga
pygame.draw.circle(screen, [255, 45, 0], [155,230], 40, 0)#joonistab kolmanda ringi ja täidab selle värviga
pygame.draw.polygon(screen, [222, 222, 222], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)
pygame.display.flip()#värskendab akna
#hoiab akna lahti
running = True
while running:#teeb tsükli
    for event in pygame.event.get():#kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT:#kui programm pannakse kinni läheb ka pygame kinni
            running == False