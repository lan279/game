import pygame
import env

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,bullet_group):

        super().__init__()
        self.image = pygame.image.load('static/bullet.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y

        self.bullet_group = bullet_group

        self.v = 10

        self.bullet_group.add(self)

    # let it move
    def update(self):
        self.rect.y -= self.v
        if self.rect.bottom  <= 0:
            self.kill()