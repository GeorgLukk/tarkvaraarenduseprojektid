import pygame,random
pygame.init()
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")

teeX,teeY = 0,400
posX,posY = 330, 330
speedX, speedY = 3, 3
coords = []
for i in range (10):
    posX = random.randint(1,posX)
    posY = random.randint(1,posY)
    speed = random.randint(1, 3)
    coords.append([posX, posY,speed])


#piltide lisamine
tee = pygame.image.load("img/tee.jpg")
s_auto = pygame.image.load("img/sauto.png")
p_auto = pygame.image.load("img/pauto.png")
tee = pygame.transform.scale(tee, [640, 480])
s_auto = pygame.transform.scale(s_auto, [70, 100])
p_auto = pygame.transform.scale(p_auto, [70, 100])
screen.blit(tee,[0,0])
screen.blit(s_auto,[100,100])
screen.blit(p_auto,[320,240])










pygame.display.flip()
running = True
while running:#teeb tsükli
    for event in pygame.event.get():#kui alustatakse programm siis alustatakse pygame
        if event.type == pygame.QUIT:#kui programm pannakse kinni läheb ka pygame kinni
            running = False
pygame.quit()