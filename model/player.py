import pygame
import env
import random
from model.player_bullet import PlayerBullet

class Player(pygame.sprite.Sprite):
    def __init__(self,player_bullet_group):
        super().__init__()

        # given a initial value
        self.v = 8
        self.live = 5

        self.image = pygame.image.load("static/rocket-64.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = env.width // 2
        self.rect.bottom = env.height 

        self.player_bullet_group = player_bullet_group

    
    # let it move
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.v 
        if keys[pygame.K_d] and self.rect.right < env.width:
            self.rect.x += self.v
    

    def fire(self):

        # at most 5 bullet
        if len(self.player_bullet_group) < 5:
            PlayerBullet(self.rect.centerx,self.rect.top,self.player_bullet_group)
    

    def reset(self):
        self.rect.centerx = env.width//2
        self.live = 5