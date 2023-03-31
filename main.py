import pygame
from pygame.locals import *
import random
import sys
import time
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

DEBUG = False

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load("icon.png").convert_alpha())
clock = pygame.time.Clock()
font = pygame.font.Font("flappybird.otf", 60)
pipecounter = PIPESPEED - 10

player = Bird()
pipes = pygame.sprite.Group()
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
            if event.key == K_F1 and DEBUG:
                FPS -= 1
            if event.key == K_F2 and DEBUG:
                FPS += 1

    status = player.update(pipes)
    if not prevstatus:
        if status:
            pipes.empty()
            scoreboxes.empty()
            pipecounter = PIPESPEED - 10
            score = 0

    if status:
        pipes.update()
        if scoreboxes.sprite:
            scored = scoreboxes.sprite.update()
        else:
            scored = False
    else:
        scored = False

    screen.fill(BLACK)
    screen.blit(back, (0,0))
    pipes.draw(screen)
    screen.blit(player.image, player.rect)

    if scored:
        score += 1
    
    
    if DEBUG:
        if scoreboxes.sprite:
            src = pygame.Surface((scoreboxes.sprite.rect.width, scoreboxes.sprite.rect.height), flags=SRCALPHA)
            src.fill((255,255,0,128))
            screen.blit(src, scoreboxes.sprite.rect)
            del src
        
        for pipe in pipes.sprites():
            src = pygame.Surface((pipe.rect.width, pipe.rect.height), flags=SRCALPHA)
            src.fill((255,50,50,128))
            screen.blit(src, pipe.rect)
            del src
        
        src = pygame.Surface((player.rect.width, player.rect.height), flags=SRCALPHA)
        src.fill((50,50,255,128))
        screen.blit(src, player.rect)
        del src

    scoretext = font.render("Score " + str(score), True, WHITE)
    screen.blit(scoretext, (310 - scoretext.get_rect().width, 10))

    pygame.display.flip()
    
    sys.stdout.write(("X Position: " + str(player.x)).ljust(8) + 
            ("; Y Position: " + str(player.y)).ljust(8) + 
            ("; Y Velocity: " + str(player.yvel)).ljust(8) + 
            ("; FPS: " + str(FPS)).rjust(3) + "\r")
    
    if status:
        pipecounter += 1
    if pipecounter == PIPESPEED:
        pipecounter = 0
        midheight = random.randint(60, 330)
        pipes.add(Pipe(midheight - 50, False), Pipe(midheight + 50, True))
        scoreboxes.add(Scorebox())
    if FPS != 0:
        clock.tick(FPS)
    else:
        time.sleep(5)

pygame.quit()
