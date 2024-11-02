import pygame
import env
from model.alien import Alien


class Game:
    def __init__(self,player,alien_group,player_bullet_group,alien_bullet_group,display_surface):
        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        self.display_surface = display_surface

        self.round = 1
        self.score = 0

        self.font = pygame.font.Font("static/font.ttf",40)
    
    def check_game_over(self):
        if self.player.live <= 0:
            self.pause()
    
    def check_alien_cross_line(self):
        for alien in self.alien_group.sprites():
            if alien.rect.bottom >=  env.height - 100:
                self.player.live -= 1
                live_text = self.font.render(f"Live : {self.player.live}",True,(0,0,0))
                alien.kill()

    def check_player_bullet_collision(self):
        if pygame.sprite.groupcollide(self.player_bullet_group,self.alien_group,True,True):
            self.score +=1
            score_text = self.font.render(f"Score : {self.score}",True,(0,0,0))
    
    def check_alien_bullet_collision(self):
        if pygame.sprite.spritecollide(self.player,self.alien_bullet_group,True):
            self.player.live -= 1
            live_text = self.font.render(f"Live : {self.player.live}",True,(0,0,0))
    
    def update(self):
        self.shift_alien()
        self.check_player_bullet_collision()
        self.check_alien_bullet_collision()
        self.check_alien_cross_line()
        self.check_game_over()
        self.win()

    def alien_grid(self):
        return [
            [
                [1,1,1,1,1,1,1,1,1,1,1],
                [0,0,0,1,1,1,1,1,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1],
                [0,1,1,1,0,0,0,1,1,1,0],
                [0,0,1,0,0,0,0,0,1,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,1,1,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,1,1,0,0]
            ]
        ]

    def win(self):
        if len(self.alien_group.sprites()) == 0 and self.player.live > 0 and self.round < 5:
            self.round += 1
            is_pause = True
            while is_pause:
                self.display_surface.fill((255,255,255))
                title_text = self.font.render(f"ROUND {self.round}",True,(255,50,50))
                title_rect = title_text.get_rect()
                title_rect.center = (env.width//2,env.height//2 - 30)

                continue_text = self.font.render("Click any place to play again",True,(0,0,0))
                continue_rect = continue_text.get_rect()
                continue_rect.center = (env.width//2,env.height//2 + 30)

                self.display_surface.blit(title_text,title_rect)
                self.display_surface.blit(continue_text,continue_rect)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        env.running = False
                        is_pause = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        round_text = self.font.render(f"Round : {self.round}",True,(0,0,0))

                        is_pause = False
                        for bullet in self.alien_bullet_group.sprites():
                            bullet.kill()
                        for bullet in self.player_bullet_group.sprites():
                            bullet.kill()
                        self.score = 0
                        self.new_round()
                        self.player.reset()

        if len(self.alien_group.sprites()) == 0 and self.player.live > 0 and self.round == 5:
            is_pause = True
            while is_pause:
                self.display_surface.fill((255,255,255))
                title_text = self.font.render(f"YOU WIN",True,(255,50,50))
                title_rect = title_text.get_rect()
                title_rect.center = (env.width//2,env.height//2 - 30)

                continue_text = self.font.render("Click any place to play again",True,(0,0,0))
                continue_rect = continue_text.get_rect()
                continue_rect.center = (env.width//2,env.height//2 + 30)

                self.display_surface.blit(title_text,title_rect)
                self.display_surface.blit(continue_text,continue_rect)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        env.running = False
                        is_pause = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.round = 1  # 五回合結束也回到 1
                        round_text = self.font.render(f"Round : {self.round}",True,(0,0,0))

                        is_pause = False
                        for bullet in self.alien_bullet_group.sprites():
                            bullet.kill()
                        for bullet in self.player_bullet_group.sprites():
                            bullet.kill()
                        self.score = 0
                        self.new_round()
                        self.player.reset()

    
    def new_round(self):
        grid = self.alien_grid()[self.round -1]
        for j,row in enumerate(grid):
            for i,col in enumerate(row):
                if col == 1:
                    alien = Alien(60+i*70,j*50,3,self.alien_bullet_group)
                    self.alien_group.add(alien)


    

    
    def shift_alien(self):

        shift = False
        for alien in self.alien_group.sprites():
            if alien.rect.left <=  0 or alien.rect.right >= env.width:
                shift = True
        
        if shift:
            for alien in self.alien_group.sprites():
                alien.direction *= -1
    
    def draw(self):
        score_text = self.font.render(f"Score : {self.score}",True,(0,0,0))
        score_rect = score_text.get_rect()
        score_rect.topleft = (30,30)

        round_text = self.font.render(f"Round : {self.round}",True,(0,0,0))
        round_rect = round_text.get_rect()
        round_rect.centerx = env.width//2
        round_rect.top = 30

        live_text = self.font.render(f"Live : {self.player.live}",True,(0,0,0))
        live_rect =  live_text.get_rect()
        live_rect.topright = (env.width - 30,30)

        self.display_surface.blit(score_text,score_rect)
        self.display_surface.blit(round_text,round_rect)
        self.display_surface.blit(live_text,live_rect)

        pygame.draw.line(self.display_surface,(255,50,50),(0,env.height - 100),(env.width,env.height - 100),3)
    
    def pause(self):
        is_pause = True
        while is_pause:

            self.display_surface.fill((255,255,255))

            game_over_text = self.font.render("GAME OVER",True,(255,50,50))
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (env.width//2,env.height//2 - 30)

            continue_text = self.font.render("Click any place to play again",True,(0,0,0))
            continue_rect = continue_text.get_rect()
            continue_rect.center = (env.width//2,env.height//2 + 30)

            self.display_surface.blit(game_over_text,game_over_rect)
            self.display_surface.blit(continue_text,continue_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    env.running = False
                    is_pause = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_pause = False
                    self.round = 1   # game over round 回到 1
                    for alien in self.alien_group:
                        alien.reset()
                    for bullet in self.alien_bullet_group.sprites():
                        bullet.kill()
                    for bullet in self.player_bullet_group.sprites():
                        bullet.kill()
                    self.score = 0
                    self.new_round()
                    
                    self.player.reset()