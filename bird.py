import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        self.prevscore = False
        self.active = False
        self.dead = False
        self.x = 160
        self.y = 245
        self.xmod = -22
        self.ymod = -15
        self.w = 43
        self.h = 30
        self.rot = 0
        self.yvel = 0
        self.g = .5
        self.origimage = pygame.image.load("bird.png").convert_alpha()
        self.updaterect()
        pygame.sprite.Sprite.__init__(self)

    def jump(self):
        if not self.active:
            self.active = True
            self.y = 245
            self.prevdead = self.dead
            self.dead = False
        if not self.dead:
            self.yvel = -6
    
    def update(self, sprites):
        if self.active:
            self.yvel += self.g
            self.y += self.yvel
            self.rot = self.yvel*-10
            if self.rot < -70 and not self.dead:
                self.rot = -70
            self.updaterect()
            if self.y > 390:
                if not self.dead:
                    self.kill()
                else:
                    self.active = False
                self.y = 390
            if not self.prevdead:
                if len(pygame.sprite.spritecollide(self, sprites, False)) != 0:
                    self.kill()

        self.prevdead = self.dead
        if self.dead:
            return False
        elif not self.active:
            return False
        else:
            return True
                
    def updaterect(self):
        self.rect = pygame.Rect(self.x + self.xmod, self.y + self.ymod, self.w, self.h)
        self.image = pygame.transform.rotate(self.origimage, self.rot)

    def kill(self):
        self.dead = True
