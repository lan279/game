import pygame
import env
import random
from model.alien_bullet import AlienBullet

class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y,v,alien_bullet_group):
        super().__init__()

        self.image = pygame.image.load('static/alien.png')
        self.rect = self.image.get_rect()

        self.v = v 

        self.starting_x = x
        self.starting_y = y 

        self.rect.center = (x,y)

        self.direction = 1
        self.alien_bullet_group = alien_bullet_group




    def update(self):
        self.rect.x += (self.direction * self.v )
        # if random.randint(1,1000) > 700:
        self.rect.y += 1
        if random.randint(1,2000) > 1999:
            self.fire()

    def fire(self):
        AlienBullet(self.rect.centerx,self.rect.bottom,self.alien_bullet_group)

    def reset(self):
        self.kill()