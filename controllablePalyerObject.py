import pygame as pg
from physicalObject import physicalObject
from Control import Control
from Live import Live
class controllablePalyerObject(Live):

    def __init__(self, id, resolution:tuple, animations,initialPosition = (0,0), initialSprite="initial", FPS = 60, puntoVida=60):
        super().__init__(id, resolution, animations, initialPosition=initialPosition, initialSprite=initialSprite, FPS=FPS, puntoVida=puntoVida)
        self.control = None

    def update(self):
        super().update()
        if not(self.control):
            self.control = Control.create()
