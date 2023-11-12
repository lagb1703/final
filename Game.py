from Observables import Observable
import os
from Control import Control
from Object import Object, Objects
from Layers import Layer
from physicalObject import physicalObject
from Playes import kirby
from Alarm import Alarm
import pygame as pg
import sys

class Game(Observable):

    game = None

    def __init__(self, resolution:tuple):
        super().__init__()
        self.time = 0
        self.resolution = resolution
        self.FPS = 60
        self.__objects = []
        self.__exit = False
        self.inputs = []
        self.display = None
        self.__layers = [None, None, None, None, None, None]

    @staticmethod
    def create(resolution:tuple = (1024, 720)):
        if not(Game.game):
            Game.game = Game(resolution)
        return Game.game

    def exit(self):
        self.__exit = True

    def notifyAll(self):
        for i in self.looking:
            if i.isTime(self.time/self.FPS):
                i.notify(self.time/self.FPS)
                if not(i.isRepeat()):
                    self.removeObserver(id = i.id)

    def gameLoop(self):
        pg.init()
        self.display = pg.display.set_mode(self.resolution)
        os.environ["SDL_VIDEO_CENTERED"] = '1'
        clock = pg.time.Clock()
        control = Control.create()
        while not(self.__exit):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            self.display.fill((255, 255, 255))
            clock.tick(self.FPS)
            self.notifyAll()
            collector = [[], [], self.time/self.FPS]
            for i in self.__objects:
                i.update(colector=collector)
            for i in collector[0]:
                self.addObserver(i)
            for i in collector[1]:
                self.getObjectsGroup(i[1]).add(i[0])
                self.addObjectInLayer(i[0], i[2])
            for i in self.__layers:
                if i:
                    i.draw(self.display, self.time)
            self.time += 1
            pg.display.update()

    def __inputTypeCorrection(self):
        pass

    def pause(self):
        pass

    def addObjectsGroup(self, Group):
        self.__objects.append(Group)

    def getObjectsGroup(self, name):
        for element in self.__objects:
            if element.groupName == name:
                return element

    def addObjectInLayer(self, object:object, z=0):
        if self.__layers[z]:
            self.__layers[z].add(object)
            return
        self.__layers[z] = Layer(z)
        self.__layers[z].add(object)

    def addObjectsInLayer(self, objects:Objects, z=0):
        if self.__layers[z]:
            for i in objects.sprites():
                self.__layers[z].add(i)
            return
        self.__layers[z] = Layer(z)
        for i in objects.sprites():
                self.__layers[z].add(i)

    def removeObject(self):
        pass

    def loadGame(self):
        pass

    def rescale(self, newResolution):
        self.resolution = newResolution
        self.display = pg.display.set_mode(newResolution)

g:Game = Game.create(resolution=(720, 460))



imagen1 = pg.surface.Surface((100, 100))
imagen1.fill("BLACK")

di = {"initial":[[imagen1], 0]}

suelo = Objects("suelo")
suelo.add(Object(1, (500, 100), di, (25, 300)))
#suelo.add(Object(2, (500, 100), di, (101, 100)))
g.addObjectInLayer(suelo, z=1)
g.addObjectsGroup(suelo)


playerObjects = Objects("Player")
player = kirby({"suelo":suelo})
playerObjects.add(player)
g.addObjectsGroup(playerObjects)
g.addObjectsInLayer(playerObjects)
g.addObjectsGroup(Objects("bullets"))


g.gameLoop()