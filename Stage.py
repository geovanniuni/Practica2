import pygame

class Stage(pygame.sprite.Sprite):

    def __init__(self, x, y, pos_x, pos_y, color):
        self.image = pygame.Surface([x,y])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.win.blit(self.image, (self.x, self.y))

