import pygame
from pygame import cursors
import pygame.locals
from Stage import Stage



pygame.init()

#pantalla = pygame.display.set_mode((600,600))

# pantalla = pygame.display.set_mode((600,600))


# b=pygame.sprite.Sprite()
# b.image = pygame.image.load("mario_3.png").convert_alpha()

# y1=b.image.subsurface((137,355,32,40)) 
# y2=b.image.subsurface((114,355,32,40))
# y3=b.image.subsurface((91,355,32,40))
# y4=b.image.subsurface((50,355,32,40))

# y5=b.image.subsurface((236,355,32,40))
# y6=b.image.subsurface((213,355,32,40))
# y7=b.image.subsurface((190,355,32,40))
# y8=b.image.subsurface((167,355,32,40))

# listaMario=[]
# listaMario.append(y1)
# listaMario.append(y2)
# listaMario.append(y3)
# listaMario.append(y4)
# listaMario.append(y8)
# listaMario.append(y7)
# listaMario.append(y6)
# listaMario.append(y5)

BLACK = (0,0,0)
clock = pygame.time.Clock()
ejecutando=True

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width,screen_height)) 

stage = Stage(50,50,100,100,(255,255,255)) 
background= pygame.image.load("Level_04.png")

stage_group = pygame.sprite.Group()
stage_group.add(Stage)

# i=0
# x=320
# temp=1
while ejecutando:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando=False
                
    
    # keys=pygame.key.get_pressed()
    
    # if keys[pygame.K_LEFT]:
        
    #     i=i+1
    #     if(i==8):
    #         i=0
    #     x=x-5
    
    # if keys[pygame.K_RIGHT]:
       
    #     i=i+1
    #     if(i==8):
    #         i=0
    #     x=x+5
        
   
    # pantalla.fill(BLACK)
    # pantalla.blit(listaMario[i],(x,200))
    
    
    pygame.display.flip()
    screen.blit(background,(0,0,0))
    stage_group.draw(screan)


    clock.tick(60)



#pantalla.fill(BLACK)
#pygame.display.flip()

pygame.quit()