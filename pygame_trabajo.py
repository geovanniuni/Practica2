import pygame
import pygame.locals

pygame.init()

#pantalla = pygame.display.set_mode((600,600))

pantalla = pygame.display.set_mode((600,600))


b=pygame.sprite.Sprite()
b.image = pygame.image.load("E:\mario_3.png").convert_alpha()

y1=b.image.subsurface((137,355,32,40))
y2=b.image.subsurface((114,355,32,40))
y3=b.image.subsurface((91,355,32,40))
y4=b.image.subsurface((50,355,32,40))

listaMario=[]
listaMario.append(y1)
listaMario.append(y2)
listaMario.append(y3)
listaMario.append(y4)


BLACK = (0,0,0)
clock = pygame.time.Clock()
ejecutando=True


i=0
x=320
temp=1
while ejecutando:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando=False
                
                
                
    
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        temp=1
        i=i+1
        if(i==4):
            i=0
        x=x-5
        
    if temp==1:
        pantalla.fill(BLACK)
        pantalla.blit(listaMario[i],(x,200))
    
    
    pygame.display.flip()
    clock.tick(15)



#pantalla.fill(BLACK)
#pygame.display.flip()

pygame.quit()