import pygame as pg
from physicalObject import physicalObject
from Control import Control
class controllablePalyerObject(physicalObject):

    def __init__(self, id, resolution:tuple, animations,initialPosition = (0,0), initialSprite="initial", FPS = 60):
        super().__init__(id, resolution, animations, initialPosition=initialPosition, initialSprite=initialSprite, FPS=FPS)
        self.control = None

    def update(self):
        if not(self.control):
            self.control = Control.create()
