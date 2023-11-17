from physicalObject import physicalObject
from Object import Objects
import pygame as pg
import math

load = pg.image.load

class Bullet(physicalObject):

    def __init__(self, id, resolution:tuple, animations, velocidad:tuple, objectivos:Objects, inpactFuntion, initialPosition = (0,0), initialSprite="initial", FPS = 60):
        super().__init__(id, resolution, animations, 
        initialPosition=initialPosition, initialSprite=initialSprite, FPS=FPS)
        self.initialSpeed[0] = velocidad[0]
        self.initialSpeed[1] = velocidad[1]

    def update(self, colector=None):
        self.linearSpeed()

class PlayerBullet(Bullet):

    def __init__(self, id, direccion, objectivos:Objects, inpactFuntion, initialPosition = (0,0), FPS = 60):
        Sprite = [[load("./sprites/Kirby/bala.png").convert_alpha()], 0]
        super().__init__(id, (10, 5),{"initial":Sprite}, (10*direccion, 0), objectivos, inpactFuntion,initialPosition=initialPosition, FPS=FPS)
        self.direction = direccion