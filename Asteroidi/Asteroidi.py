import random, pygame, sys
from random import *
from pygame.locals import *
import time

def kraj():
    for i in range(4):
        DISPLAYSURF.fill(WHITE)
        pygame.display.update()
        pygame.time.wait(300)
        DISPLAYSURF.fill(BLACK)
        pygame.display.update()
        pygame.time.wait(300)
    done = "Kraj Igre! Preživjeli ste %s sekundi." % (counting_time)
    fontObj = pygame.font.SysFont('Arial', 23)
    textSurfaceObj = fontObj.render(done , True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (500,400)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    

def pocetak(filename, restart):
    if restart == True:
     pygame.mixer.music.load(filename)
     pygame.mixer.music.play(-1)
     DISPLAYSURF.fill(BLACK)
    pygame.display.update()
    DISPLAYSURF.blit(three, (250,200))
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.fill(BLACK)
    pygame.display.update()
    DISPLAYSURF.blit(two, (250,200))
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.blit(one, (250,200))
    pygame.display.update()
    pygame.time.wait(1000)


    

FPS = 20
WINDOWWIDTH = 1200
WINDOWHEIGHT = 800
BOXSIZE = 40

RED = (255, 0, 0 )
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0 , 0 ,0 )
YELLOW = (255, 255, 0)
highscore = 0

pygame.init()
pygame.mixer.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))




pygame.display.set_caption("Asteroidi!")
box = []
coords = []
i = 0
click = False
restart = False
mouse = pygame.image.load('space.jpg')
mouse = pygame.transform.scale(mouse, (40, 40))
boom = pygame.image.load('eksplozija.jpg')
boom = pygame.transform.scale(boom, (333,333))



start = "Koristite miš"
start1 = "da izbjegnete asteroide"
start2 = "Kliknite da krenete"
fontObj = pygame.font.SysFont('Arial', 20)
textSurfaceObj = fontObj.render(start , True, WHITE, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400,200)
DISPLAYSURF.blit(textSurfaceObj,textRectObj)
textSurfaceObj1 = fontObj.render(start1 , True, WHITE, BLACK)
textRectObj1 = textSurfaceObj.get_rect()
textRectObj1.center = (400,300)
DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
textSurfaceObj2 = fontObj.render(start2 , True, WHITE, BLACK)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (400,360)
DISPLAYSURF.blit(textSurfaceObj2,textRectObj2)


pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            click = True
    if click == True:
        break


mousex = 350
mousey = 500
j = 0

start_time = pygame.time.get_ticks()
while True:

    if restart == True:
        box = []
        coords = []
        i = 0
        click = False
        restart = False
        start_time = pygame.time.get_ticks()
        
    
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(mouse, (mousex-20, mousey))
    counting_time = (pygame.time.get_ticks() - start_time)/1000
    string = "Time: %s" % (counting_time)
    fontObj = pygame.font.SysFont('Cooper Black', 35)
    textSurfaceObj = fontObj.render( string , True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (100,200)

    if highscore == 0:
        
        string1 = "Highscore: %s" % (counting_time)
    elif counting_time > highscore:
        string1 = 'Highscore %s' % (counting_time)
    else:
        string1 = "Highscore: %s" % (highscore)
        
    fontObj1 = pygame.font.SysFont('Cooper Black', 35)
    textSurfaceObj1 = fontObj1.render(string1 , True, WHITE, BLACK)
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (150,100)
    x = randrange(0,800)
    y = randrange(0,50)

   
    if i%100 == 0 and i!= 0:
        del coords [:45]
        del box [:45]
        i -= 45
        j -= 45
        
    
    box.append(pygame.Rect(x, y, BOXSIZE, BOXSIZE))

    point1 = list(box[i].bottomleft)
    point2 = list(box[i].bottomright)
    coords.append([point1,point2])
    
    pygame.time.wait(10)
    for j in range(len(box)):

        if restart == True:
            break
    
        pygame.draw.rect(DISPLAYSURF, YELLOW, box[j])
        box[j].centery +=10
        coords[j][0][1] +=10

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
        if ( (coords[j][0][0]<= mousex <=coords[j][1][0]) and (coords[j][0][1]-30 <= mousey <= coords[j][0][1])):
            pygame.mixer.music.stop()
            DISPLAYSURF.blit(boom, (mousex-20, mousey))
            pygame.mixer.music.load('eksplozija.mp3')
            pygame.mixer.music.play(-1)
            pygame.display.update()
            time.sleep(1.0)
            pygame.mixer.music.stop()
            
            kraj()
            click = False
            while 1 and restart == False:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEMOTION:
                        mousex, mousey = event.pos

                again = "Igraj opet?" 
                fontObj1 = pygame.font.SysFont('Arial', 20)
                textSurfaceObj1 = fontObj1.render(again , True, WHITE, BLACK)
                textRectObj1 = textSurfaceObj1.get_rect()
                textRectObj1.center = (400,350)
                DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
                pygame.display.update()
                
                while (300<= mousex <= 400 and 350<=mousey <=400) and restart == False:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEMOTION:
                            mousex, mousey = event.pos
                        elif event.type == MOUSEBUTTONUP:
                            click = True
                            
                    again = "Igraj opet?" 
                    fontObj1 = pygame.font.SysFont('Arial', 20)         
                    textSurfaceObj1 = fontObj1.render(again , True, WHITE, YELLOW)
                    textRectObj1 = textSurfaceObj1.get_rect()
                    textRectObj1.center = (400,350)
                    DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
                    pygame.display.update()

                    if click == True:
                        restart = True
                        highscore = counting_time
                        start_time = 0
                        break
                    
                    else:
                        
                        continue
                   
        
        
    i+=1
    pygame.display.update()
    FPSCLOCK.tick(FPS)




        
