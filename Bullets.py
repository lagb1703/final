from physicalObject import physicalObject
from Object import Objects
import pygame as pg
import math

class Bullet(physicalObject):

    def __init__(self, id, resolution:tuple, animations, velocidad:tuple
    , daño:int, objectivos:Objects, initialPosition = (0,0), initialSprite="initial", FPS = 60):
        super().__init__(id, resolution, animations, 
        initialPosition=initialPosition, initialSprite=initialSprite, FPS=FPS)
        self.initialSpeed[0] = velocidad[0]
        self.initialSpeed[1] = velocidad[1]

    def update(self, colector=None):
        self.linearSpeed()