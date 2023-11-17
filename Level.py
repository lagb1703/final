import pygame as pg
from Camera import Camera
from Observables import Observable
from Object import Objects
from GUI import GUI

class Level(GUI, Observable):

    def __init__(self, display:pg.surface.Surface, backgroud:pg.surface.Surface, camara:Camera, resolution=(720, 420), screenResolution=(720, 420), layers=7, FPS=60):
        Observable.__init__(self)
        GUI.__init__(self, display, backgroud, resolution=resolution, layers=layers)
        self.screenResolution = screenResolution
        self.__objects = {}
        self.__cameraOldPosition = [camara.x, camara.y]
        self._camara = camara
        self.time = 0
        self.FPS = FPS
        self.__scales:tuple = (resolution[0]*screenResolution[0]/camara.resolution[0], resolution[1]*screenResolution[1]/camara.resolution[1])

    def addObjectsGroup(self, Group:Objects):
        self.__objects[Group.groupName] = Group

    def getObjectsGroup(self, name:str):
        if not(self.__objects.get(name)):
            self.__objects[name] = Objects(name)
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
        distanciaX = 0
        distanciaY = 0
        if self._camara.x + self._camara.resolution[0] < self.resolution[0]:
            self._camara.x += 1
            distanciaX = self.__cameraOldPosition[0] - self._camara.x
        if self._camara.y < self.resolution[1]:
            distanciaY = self.__cameraOldPosition[1] - self._camara.y
        self._backgroudPosition = (self._backgroudPosition[0] + distanciaX/90,
        self._backgroudPosition[1] + distanciaY/90)
        return (distanciaX, distanciaY)


    def logic(self, nextGui=None):
        # distancia = self.cameraMove()
        self._display.blit(self._backgroud, self._backgroudPosition)
        for i in self.getLayers():
            if i:
                i.draw(self._display, self.time)
        #         i.moveAllDistance(distancia)
        # newDisplay = pg.transform.scale(self._display, self.__scales)
        # self._display.fill((0,0,0,0))
        # self._display.blit(newDisplay, (0,0))
        pg.display.update()
        self.notifyAll()
        collector = [[], [], self.time/self.FPS]
        for i in self.__objects.values():
            i.update(colector=collector)
        for i in collector[0]:
            self.addObserver(i)
        for i in collector[1]:
            self.getObjectsGroup(i[1]).add(i[0])
            self.addObjectInLayer(i[0], i[2])
        self.time += 1
