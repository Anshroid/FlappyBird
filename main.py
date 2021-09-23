import pygame
from pygame.locals import *
import random
from bird import Bird
from pipe import Pipe
from scorebox import Scorebox

WIDTH = 320
HEIGHT = 490
FPS = 60
PIPESPEED = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load("icon.png").convert_alpha())
clock = pygame.time.Clock()
font = pygame.font.Font("flappybird.otf", 60)
pipecounter = PIPESPEED - 10

player = Bird()
all_sprites = pygame.sprite.Group()
scoreboxes = pygame.sprite.GroupSingle()
score = 0

back = pygame.transform.scale(pygame.image.load("background.jpg").convert(), (WIDTH, HEIGHT))

status = False
running = True
while running:
    prevstatus = status
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE: 
                player.jump()
            if event.key == K_F4:
                if pygame.key.get_pressed()[K_LALT]:
                    running = False
    
    status = player.update(all_sprites)
    if not prevstatus:
        if status:
            all_sprites.empty()
            scoreboxes.empty()
            pipecounter = PIPESPEED - 10
            score = 0
    
    if status:
        all_sprites.update()
        if scoreboxes.sprite:
            scored = scoreboxes.sprite.update()
        else:
            scored = False
    else:
        scored = False
        
    screen.fill(BLACK)
    screen.blit(back, (0,0))
    all_sprites.draw(screen)
    screen.blit(player.image, player.rect)

    if scored:
        score += 1
    
    if scoreboxes.sprite:
        src = pygame.Surface((scoreboxes.sprite.rect.width, scoreboxes.sprite.rect.height), flags=SRCALPHA)
        src.fill((255,255,0,128))
        #screen.blit(src, scoreboxes.sprite.rect)
        del src
        
    #src = pygame.Surface((WIDTH, 270), flags=SRCALPHA)
    #src.fill((255,0,0,128))
    #screen.blit(src, (0, 60))
    #del src

    scoretext = font.render("Score " + str(score), True, WHITE)
    screen.blit(scoretext, (310 - scoretext.get_rect().width, 10))
    
    pygame.display.flip()
    #print(clock.get_fps())
    if status:
        pipecounter += 1
    if pipecounter == PIPESPEED:
        pipecounter = 0
        midheight = random.randint(60, 330)
        all_sprites.add(Pipe(midheight - 50, False), Pipe(midheight + 50, True))
        scoreboxes.add(Scorebox())
    clock.tick(FPS)

pygame.quit()
