import pygame as pg
from Camera import Camera
from Observables import Observable
from Object import Objects
from GUI import GUI

class Level(GUI, Observable):

    def __init__(self, display:pg.surface.Surface, backgroud:pg.surface.Surface, camara:Camera, resolution=(720, 460), layers=7):
        Observable.__init__()
        self.__exit = False
        self._display:pg.surface.Surface = display
        self._backgroud:pg.surface.Surface = pg.transform.scale(backgroud, resolution)
        self.resolution = resolution
        self.__layers = [None]*layers
        self._backgroudInitial:pg.surface.Surface = backgroud
        self.__numberLayers = layers
        self.__objects = {}
        self.__cameraOldPosition = [camara.x, camara.y]
        self._camara = camara
        self.time = 0
        self.__scales:tuple = (resolution[0]/camara.resolution[0], resolution[1]/camara.resolution[1])

    def addObjectsGroup(self, Group:Objects):
        self.__objects[Group.groupName] = Group

    def getObjectsGroup(self, name:str):
        return self.__objects[name]

    def removeObjectsGroup(self, name:str):
        del self.__objects[name]

    def notifyAll(self):
        for i in self.looking:
            if i.isTime(self.time/self.FPS):
                i.notify(self.time/self.FPS)
                if not(i.isRepeat()):
                    self.removeObserver(id = i.id)

    def cameraMove(self):
        self._camara.update()
        distanciaX = self._camara.x - self.__cameraOldPosition[0]
        distanciaY = self._camara.y - self.__cameraOldPosition[1]
        self._backgroudPosition = (self._backgroudPosition[0] + distanciaX,
        self._backgroudPosition[1] + distanciaY)
        return (distanciaX, distanciaY)


    def logic(self, nextGui=None):
        distancia = self.cameraMove()
        self._display.blit(self._backgroud, self._backgroudPosition)
        for i in self.getLayers:
            if i:
                i.draw(self.display, self.time)
                i.moveAllDistance(distancia)
        self._display = pg.transform.scale(self._display, self.__scales)
        pg.display.update()
        self.notifyAll()
        collector = [[], [], self.time/self.FPS]
        for i in self.__objects:
            i.update(colector=collector)
        for i in collector[0]:
            self.addObserver(i)
        for i in collector[1]:
            self.getObjectsGroup(i[1]).add(i[0])
            self.addObjectInLayer(i[0], i[2])
        self.time += 1
