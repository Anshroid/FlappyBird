import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, y, bottom):
        self.x = 310
        self.y = y
        self.xmod = -35
        self.ymod = 0 if bottom else -377
        self.w = 70
        self.h = 377
        self.image = pygame.transform.rotate(pygame.image.load("pipe.png").convert_alpha(), 0 if bottom else 180)
        self.updaterect()
        pygame.sprite.Sprite.__init__(self)
    
    def update(self):
        self.x -= 2
        if self.x < -80:
            self.kill()
        self.updaterect()

    def updaterect(self):
        self.rect = pygame.Rect(self.x + self.xmod, self.y + self.ymod, self.w, self.h)
