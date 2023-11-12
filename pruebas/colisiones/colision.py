import sys
import random
import pygame as pg

WIDTH, HEIGHT = 720, 400
SPEED, FPS = 5, 60

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
dino_image = pg.image.load("dino.png").convert_alpha()
dino_rect = dino_image.get_rect()
star_image = pg.image.load("star.png").convert_alpha()
star_rect = star_image.get_rect()
star_rect.center = (WIDTH//2, HEIGHT//2)
clock = pg.time.Clock()

pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
joystick = joysticks[0]

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    clock.tick(FPS)

    if joystick.get_hat(0)[0] == -1 and dino_rect.left > 0:
        dino_rect.x -= SPEED
    if joystick.get_hat(0)[0] == 1 and dino_rect.right < WIDTH:
        dino_rect.x += SPEED
    if joystick.get_hat(0)[1] == 1 and dino_rect.top > 0:
        dino_rect.y -= SPEED
    if joystick.get_hat(0)[1] == -1 and dino_rect.bottom < HEIGHT:
        dino_rect.y += SPEED

    if dino_rect.colliderect(star_rect):
        star_rect.x = random.randint(50, WIDTH - 50)
        star_rect.y = random.randint(50, HEIGHT - 50)
        print("COLISION")

    display.blit(background, (0, 0))
    display.blit(dino_image, dino_rect)
    display.blit(star_image, star_rect)

    pg.display.update()