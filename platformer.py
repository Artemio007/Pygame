import sys
import pygame
from player import *
from blocks import *
from skola import *
from bottle import *

pygame.init()

WIN_WIDTH = 1344
WIN_HEIGHT = 704
DISPLAY1 = (WIN_WIDTH, WIN_HEIGHT)
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#75c954"
score = 0
score1 = 0
f = pygame.font.SysFont('arial', 30)


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2
    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Школа vs Кирюха")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    hero = Player(1280, 50)
    left = right = False
    up = False
    hero1 = Player2(40, 50)
    leftt = rightt = False
    upt = False
    bottler = Bottle(620, 50)
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    entities.add(hero1)
    entities.add(bottler)

    level = [
        "------------------------------------------",
        "-               --    --                 -",
        "-                               -        -",
        "-               --------                 -",
        "-                                        -",
        "-      -         -       -         -     -",
        "-           -                 -          -",
        "-      -                        -        -",
        "-              -            -            -",
        "-                                        -",
        "-   -         -                -         -",
        "-                                        -",
        "-                               -        -",
        "-      -        -      -                 -",
        "-                                        -",
        "-     -               -           -      -",
        "-                                        -",
        "-      -            -           -        -",
        "-             -            -        -    -",
        "-                                        -",
        "-           -                   -        -",
        "------------------------------------------"]

    timer = pygame.time.Clock()
    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while True:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_a:
                leftt = True
            if e.type == KEYDOWN and e.key == K_d:
                rightt = True
            if e.type == KEYDOWN and e.key == K_w:
                upt = True
            if e.type == KEYUP and e.key == K_a:
                leftt = False
            if e.type == KEYUP and e.key == K_d:
                rightt = False
            if e.type == KEYUP and e.key == K_w:
                upt = False

        screen.blit(bg, (0, 0))
        f = pygame.font.SysFont('arial', 30)
        m = pygame.font.SysFont('arial', 50)

        global score
        global score1
        if sprite.collide_rect(hero1, bottler):
            score1 += 1
            bottler.die()
        if sprite.collide_rect(hero, bottler):
            score += 1
            bottler.die()

        if score1 == 10:
            sc = m.render('Kirill win!', True, (150, 75, 0))
            screen.blit(sc, (510, 200))
            time.wait(1000)

        if score == 10:
            sc = m.render('Andrey win!', True, (150, 75, 0))
            screen.blit(sc, (510, 200))
            time.wait(1000)

        view_score = f" Andrey {score}"
        view_score1 = f" Kirill {score1}"
        sc_text = f.render(str(view_score), True, (150, 75, 0))
        screen.blit(sc_text, (1160, 40))
        sc_text1 = f.render(str(view_score1), True, (150, 75, 0))
        screen.blit(sc_text1, (50, 40))

        camera.update(bottler)
        camera.update(hero)
        camera.update(hero1)
        camera.update(bottler)
        hero.update(left, right, up, platforms)
        hero1.update(leftt, rightt, upt, platforms)

        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

        if sprite.collide_rect(hero1, hero):
            if right:
                hero.rect.right = hero1.rect.left

            if left:
                hero.rect.left = hero1.rect.right

            if rightt:
                hero1.rect.right = hero.rect.left

            if leftt:
                hero1.rect.left = hero.rect.right

            if leftt and right:
                leftt = False
                right = False

            if rightt and left:
                rightt = False
                left = False


if __name__ == "__main__":
    main()
