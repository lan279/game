import pygame
import env
from model.player import Player
from model.alien import Alien
from model.alien_bullet import AlienBullet
from model.player_bullet import PlayerBullet
from model.game import Game

pygame.init()
display_surface = pygame.display.set_mode((env.width,env.height))
pygame.display.set_caption("Alien invastor")

# clock
fps = 60
clock = pygame.time.Clock()

# create group
player_bullet_group = pygame.sprite.Group()

alien_bullet_group = pygame.sprite.Group()

player_group = pygame.sprite.Group()
player = Player(player_bullet_group)
player_group.add(player)

alien_group = pygame.sprite.Group()


game = Game(player,alien_group,player_bullet_group,alien_bullet_group,display_surface)
game.new_round()


while env.running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()
    
    display_surface.fill((255,255,255))

    player_group.update()
    player_group.draw(display_surface)

    player_bullet_group.update()
    player_bullet_group.draw(display_surface)

    alien_group.update()
    alien_group.draw(display_surface)

    alien_bullet_group.update()
    alien_bullet_group.draw(display_surface)

    game.draw()
    game.update()


    clock.tick(fps)
    pygame.display.update()

pygame.quit()