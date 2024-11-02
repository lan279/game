import pygame
import env 

class AlienBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,bullet_group):
        super().__init__()

        self.image = pygame.image.load("static/bomb.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

        self.rect.centerx = x 
        self.rect.top = y 

        self.v = 10

        self.bullet_group = bullet_group
        bullet_group.add(self)


    def update(self):
        self.rect.y += self.v
        if self.rect.top >= env.height:
            self.kill()