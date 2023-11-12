import pygame as pg
from Camera import Camera
from Observables import Observable
from Object import Objects
from GUI import GUI

class Level(GUI, Observable):

    def __init__(self, display:pg.surface.Surface, backgroud:pg.surface.Surface, camara:Camera, resolution=(720, 460), layers=7):
        super().__init__(display, backgroud, layers=layers)
        Observable.__init__()
        self.__objects = {}
        self._camara = camara
        self.time = 0

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

    def logic(self):
        super().logic()
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