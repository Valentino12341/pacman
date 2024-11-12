import pygame  
import random



pygame.init()
sc = pygame.display.set_mode((800,800))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pacman.png")
        self.image = pygame.transform.scale(self.image,(30,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (300,300)
        self.speed = 5


        def update(self,keys):
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed


running = True
while running:
    sc.blit((10,10),Player)


    
