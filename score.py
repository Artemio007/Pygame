from pygame import *
COLOR = "#FF6262"
WIDTH = 10
HEIGHT = 20
score = 0


class Score(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey(Color(COLOR))

    def record(self, score):
        score += 50
