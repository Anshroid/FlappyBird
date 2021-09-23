import pygame

class Scorebox(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 310
        self.y = 0
        self.xmod = 0
        self.ymod = 0
        self.w = 1
        self.h = 490
        self.updaterect()
        pygame.sprite.Sprite.__init__(self)
    
    def update(self):
        self.x -= 2
        if self.x < -80:
            self.kill()
        self.updaterect()
        if self.x == 160:
            return True

    def updaterect(self):
        self.rect = pygame.Rect(self.x + self.xmod, self.y + self.ymod, self.w, self.h)
