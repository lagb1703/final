import sys
import random
import pygame as pg

WIDTH, HEIGHT = 720, 400
SPEED, FPS = 5, 60

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("./imagenes/grass.png").convert_alpha()
back_rect = background.get_rect()
back_rect.y = HEIGHT//2
back_rect.x = 0
dino_image = pg.image.load("./imagenes/dino.png").convert_alpha()
dino_rect = dino_image.get_rect()
dino_rect.center = (0, 0)
clock = pg.time.Clock()
px = 0
py = 0
tv = 0
th = 0
tierra = False
vertical = 30
horizontal = SPEED
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    clock.tick(FPS)
    # keys = pg.key.get_pressed()
    
    # if keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
    #     th += 1

    # if (keys[pg.K_LEFT] and horizontal > 0) or (keys[pg.K_RIGHT] and horizontal < 0):
    #     th = 0
    #     px = dino_rect.x

    # if keys[pg.K_LEFT]:
    #     horizontal = -SPEED
    # elif keys[pg.K_RIGHT]:
    #     horizontal = SPEED
    # else:
    #     px = dino_rect.x
    #     th = 0

    # if dino_rect.colliderect(back_rect):
    #     tv = 0
    #     py = dino_rect.y
    # else:
    #     tv += 1

    # if keys[pg.K_UP] and dino_rect.colliderect(back_rect):
    #     py = dino_rect.y - 1
    
    # dino_rect.x = th*horizontal + px
    # dino_rect.y = 0.045*tv**2 - vertical*(tv/10) + py

    # print(dino_rect.x, dino_rect.y)

    display.fill("BLUE")
    display.blit(background, back_rect)
    display.blit(dino_image, dino_rect)

    pg.display.update()