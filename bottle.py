from pygame import *
import os
import random


WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
ICON_DIR = os.path.dirname(__file__)
ANIMATION_STAY = [('%s/bottle/v1.png' % ICON_DIR, 0.1)]


class Bottle(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.startX = random.randint(100, 500)
        self.startY = random.randint(100, 500)
        self.goX = random.randint(100, 500)
        self.goY = random.randint(100, 600)
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.image = image.load("%s/bottle/v1.png" % ICON_DIR)
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

    def die(self):
        time.wait(10)
        self.teleporting(random.randint(100, 1250), random.randint(100, 500))