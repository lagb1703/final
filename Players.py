from controllablePlayerObject import controllablePlayerObject as cpo
import pygame as pg
from Alarm import Alarm
from Bullets import Bullet
from physicalObject import physicalObject

class LaserBeam(physicalObject):

    def __init__(self, initialPosition:tuple, direction:int, inpactFuntion=None):
        imagen = pg.surface.Surface((100, 100))
        imagen.fill((0,255,0))
        super().__init__(0, (100, 30), {"initial":[[imagen], 120]}, FPS=60, initialPosition=initialPosition)
        self.__enviado = False
        self.__tamaño = 0
        self.__direction = direction

    def update(self, colector=None):
        if not(self.__enviado):
            colector[0].append(Alarm(colector[2], 10, False, self.kill))
            self.__enviado = True
        self.__tamaño += 1
        self.image = pg.surface.Surface((self.resolution[0] + self.__tamaño, self.resolution[1]))
        if self.__direction < 0:
            self.rect.x -= 1
        self.image.fill((0, 255, 0))

class kirby(cpo):

    def __init__(self, posicion:tuple, grupos:dict):
        #imagen = pg.image.load("./sprites/Kirby/Default.png").convert_alpha()
        imagen:pg.surface.Surface = pg.image.load("./sprites/Kirby/Default.png").convert_alpha()
        super().__init__(0, (100, 70), {"initial":[[imagen], 0]}, initialPosition=posicion, FPS=60)
        self.aceleration = [0, 9.8]
        self.initialSpeed = [1, -35]
        self.grupos = grupos
        self.__dash = False
        self.__dashHabilitado = True
        self.__disparoHabilitado = True
        self.__cartas = 0
        self.__superDisparo = False

    def setDash(self, valor:bool):
        self.__dash = valor

    def __detenerDash(self):
        self.setDash(False)

    def setDisparo(self, valor):
        self.__disparoHabilitado = valor

    def __habilitarDisparo(self):
        self.setDisparo(True)

    def setSuper(self, valor):
        self.__superDisparo = valor

    def __habilitarSuper(self):
        self.setSuper(False)

    def getCartas(self):
        return self.__cartas

    def __conectaDisparo(self, enemigo):
        self.__cartas += 0.1

    def update(self, colector=None):
        super().update()
        input = self.control.getInput()
        if self.__superDisparo:
            return
        if input.ONE and self.__cartas >= 0 and not(self.__dash):
            colector[0].append(Alarm(colector[2], 10, False, self.__habilitarSuper))
            colector[1].append((LaserBeam((self.rect.x, self.rect.y), self.initialSpeed[0]), "bullets", 3))
            self.__superDisparo = True
            return

        if self.__dash:
            if self.initialSpeed[0] > 0 and not(self.collitionLeftGroup(self.grupos["suelo"], 1, salvaguarda=20)):
                if self.rect.x < 720 - self.resolution[0]:
                    self.rect.x += 5
            elif not(self.collitionRigthGroup(self.grupos["suelo"], 1, salvaguarda=20)) and self.rect.x > 0:
                self.rect.x -= 5
            return
        if not(self.collitionUpGroup(self.grupos["suelo"], 1)):
            self.gravity()
        else:
            self.__dashHabilitado = True
            if input.FOUR and not(self.collitionDownGroup(self.grupos["suelo"], 1)):
               self.rect.y -= 5
               self.initialPosition[1] = self.rect.y
               self.Time[1] = 0

        if input.THREE and self.__disparoHabilitado:
            self.__disparoHabilitado = False
            imagen = pg.surface.Surface((500, 500))
            imagen.fill((0,0,0))
            colector[0].append(Alarm(colector[2], 3.5, False, self.__habilitarDisparo))
            colector[1].append((Bullet(colector[2], (50, 10), 
            {"initial":[[imagen], 0]}, (50*self.initialSpeed[0],0), 100
            , None, initialPosition=(self.rect.x, self.rect.y), FPS=5),"bullets", 1))

        if input.TWO and self.__dashHabilitado:
            colector[0].append(Alarm(colector[2], 1, False, self.__detenerDash))
            self.__dash = True
            self.__dashHabilitado = False

        if input.LEFT and self.rect.x > 0 and not(self.collitionLeftGroup(self.grupos["suelo"], 1, salvaguarda=20)):
            self.initialSpeed[0] = -1
            self.rect.x -= 1
        
        if input.RIGTH and self.rect.x < 720 - self.resolution[0] and not(self.collitionRigthGroup(self.grupos["suelo"], 1, salvaguarda=20)):
            self.initialSpeed[0] = 1
            self.rect.x += 1