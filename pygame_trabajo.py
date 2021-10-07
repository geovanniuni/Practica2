import pygame
import pygame.locals

pygame.init()

#pantalla = pygame.display.set_mode((600,600))

pantalla = pygame.display.set_mode((900,600))


b=pygame.sprite.Sprite()
b.image = pygame.image.load("simon.png").convert_alpha()

y1=b.image.subsurface((0,0,25,50)) 
y2=b.image.subsurface((55,0,25,50))
y3=b.image.subsurface((85,0,25,50))
y4=b.image.subsurface((114,0,25,50))
y5=b.image.subsurface((145,0,25,50))
y6=b.image.subsurface((175,0,25,50))
y7=b.image.subsurface((200,0,25,50))

x1=b.image.subsurface((260,320,25,50)) 
x2=b.image.subsurface((315,320,25,50))
x3=b.image.subsurface((345,320,25,50))
x4=b.image.subsurface((364,320,25,50))
x5=b.image.subsurface((415,320,25,50))
x6=b.image.subsurface((465,320,25,50))
x7=b.image.subsurface((510,320,25,50))




listaDerecha=[]
listaDerecha.append(y1)
listaDerecha.append(y2)
listaDerecha.append(y3)
listaDerecha.append(y4)
listaDerecha.append(y5)
listaDerecha.append(y6)
listaDerecha.append(y7)

listaIzquierda=[]
listaIzquierda.append(x1)
listaIzquierda.append(x2)
listaIzquierda.append(x3)
listaIzquierda.append(x4)
listaIzquierda.append(x5)
listaIzquierda.append(x6)
listaIzquierda.append(x7)

listaCastlevania=[]
listaCastlevania.append(listaDerecha)
listaCastlevania.append(listaIzquierda)
BLACK = (0,0,0)
clock = pygame.time.Clock()
ejecutando=True


j=0
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
        
        j=j+1
        if(j==7):
            j=1
        x=x-5
        i=1
    if keys[pygame.K_RIGHT]:
       
        j=j+1
        if(j==7):
            j=1
        x=x+5
        i=0
   
    pantalla.fill(BLACK)
    pantalla.blit(listaCastlevania[i][j],(x,200))
    
    
    pygame.display.flip()
    clock.tick(10)



#pantalla.fill(BLACK)
#pygame.display.flip()

pygame.quit()