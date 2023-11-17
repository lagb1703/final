from physicalObject import physicalObject
from Object import Objects
import pygame as pg
import math

load = pg.image.load

class Bullet(physicalObject):

    def __init__(self, id, resolution:tuple, animations, velocidad:tuple, objectivos:Objects, inpactFuntion, screanResolution:tuple, initialPosition = (0,0), initialSprite="initial", FPS = 60):
        super().__init__(id, resolution, animations, 
        initialPosition=initialPosition, initialSprite=initialSprite, FPS=FPS)
        self.initialSpeed[0] = velocidad[0]
        self.initialSpeed[1] = velocidad[1]
        self.screanResolution = screanResolution
        self.__inpactFunction = inpactFuntion
        self.__objetivos = objectivos

    def getObjectivos(self):
        return self.__objetivos.sprites()

    def update(self, colector=None):
        self.linearSpeed()
        self.inpactGroup(self.__objetivos)
        if(self.rect.x < 0 or self.rect.x > self.screanResolution[0]):
            self.kill()

    def inpactGroup(self, group:Objects):
        for i in group.sprites():
            if i == self:
                continue
            solucion = self.collitionOnSprite(i)
            if solucion:
                self.__inpactFunction(i)
                self.kill()
                return

class PlayerBullet(Bullet):

    def __init__(self, id, direccion, objectivos:Objects, inpactFuntion, screanResolution:tuple, initialPosition = (0,0), FPS = 60):
        Sprite = [[load("./sprites/Kirby/bala.png").convert_alpha()], 0]
        super().__init__(id, (10, 5),{"initial":Sprite}, (60*direccion, 0), objectivos, inpactFuntion, screanResolution,initialPosition=initialPosition, FPS=FPS)
        self.direction = direccion

class zanahoriaBullet(Bullet):

    def __init__(self, id, objectivos:Objects, inpactFuntion, screanResolution:tuple, initialPosition = (0,0), FPS = 60):
        Sprite = [[load("./sprites/Zanahoria/proyectil.png").convert_alpha()], 0]
        super().__init__(id, (60, 30),{"initial":Sprite}, (10, 0), objectivos, inpactFuntion, screanResolution,initialPosition=initialPosition, FPS=FPS)
        self.__correccion = 0


    def update(self, colector=None):
        super().update(colector=colector)
        if len(self.getObjectivos()) == 0:
            return
        self.__correccion += 1
        if self.__correccion >= 60:
            self.Time[1] = 0
            self.initialPosition[1] = self.rect.y
            rest = self.rect.y - self.getObjectivos()[0].rect.y
            if rest == 0:
                self.initialSpeed[1] = 0
            else:
                self.initialSpeed[1] = -2*(rest/abs(rest))
            self.__correccion = 0

