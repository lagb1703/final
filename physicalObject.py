import pygame as pg
from Object import Object, Objects

class physicalObject(Object):
    
    def __init__(self, id, resolution:tuple, animations,initialPosition = (0,0), initialSprite="initial", FPS = 60):
        super().__init__(id, resolution, animations, initialPosition=initialPosition, initialSprite=initialSprite)
        self.aceleration = [0,0]
        self.initialSpeed = [0,0]
        self.initialPosition = [self.rect.x, self.rect.y]
        self.mask = pg.mask.from_surface(self.image)
        self.Time = [0,0]
        self.FPS = FPS
        self.direction = 1
        self.__aplicado = False

    def gravity(self):
        self.Time[1] += 1
        self.rect.y = (self.aceleration[1]/2)*(self.Time[1]/self.FPS)**2 + self.initialSpeed[1]*(self.Time[1]/self.FPS) + self.initialPosition[1]

    def linearSpeed(self):
        self.Time[0] += 1
        self.Time[1] += 1
        self.rect.x = self.initialSpeed[0]*(self.Time[0]/self.FPS) + self.initialPosition[0]
        self.rect.y = self.initialSpeed[1]*(self.Time[1]/self.FPS) + self.initialPosition[1]

    def collitionUpSprite(self, object:Object, distance:int)->bool:
        #print(object.rect.x, self.rect.x)
        if not((object.rect.x <= self.rect.x <= object.rect.x + object.resolution[0]) 
        or (object.rect.x <= self.rect.x + self.resolution[0] <= object.rect.x + object.resolution[0])):
            return False
        #print(object.rect.y, self.rect.y)
        if not(object.rect.y >= self.rect.y + self.resolution[1] >= object.rect.y - distance):
            return False
        return True

    def collitionDownSprite(self, object:Object, distance:int)->bool:
        if not((object.rect.x <= self.rect.x <= object.rect.x + object.resolution[0]) 
        or (object.rect.x <= self.rect.x + self.resolution[0] <= object.rect.x + object.resolution[0])):
            return False
        if not(object.rect.y + distance <= self.rect.y ):
            return False
        return True
    
    def collitionRigthSprite(self, object:Object, distance:int, salvaguarda:int = 10)->bool:
        if (object.rect.y - object.resolution[1] > self.rect.y - salvaguarda < object.rect.y) and (object.rect.y - object.resolution[1] > self.rect.y - self.resolution[1] < object.rect.y):
            return False
        if not(object.rect.x + object.resolution[0] > self.rect.x + self.resolution[0] + distance > object.rect.x):
            return False
        return True

    def collitionLeftSprite(self, object:Object, distance:int, salvaguarda:int = 10)->bool:
        if (object.rect.y - object.resolution[1] > self.rect.y - salvaguarda < object.rect.y) and (object.rect.y - object.resolution[1] > self.rect.y - self.resolution[1] < object.rect.y):
            return False
        if not(object.rect.x < self.rect.x - distance < object.rect.x + object.resolution[0]):
            return False
        return True

    def collitionUpGroup(self, group:Objects, distance:int):
        for i in group.sprites():
            solucion = self.collitionUpSprite(i, distance)
            if solucion:
                return solucion
        return False
    
    def collitionDownGroup(self, group:Objects, distance:int):
        for i in group.sprites():
            solucion = self.collitionDownSprite(i, distance)
            if solucion:
                return solucion
        return False

    def collitionLeftGroup(self, group:Objects, distance:int, salvaguarda:int = 10):
        for i in group.sprites():
            solucion = self.collitionLeftSprite(i, distance, salvaguarda=salvaguarda)
            if solucion:
                return solucion
        return False

    def collitionRigthGroup(self, group:Objects, distance:int, salvaguarda:int = 10):
        for i in group.sprites():
            solucion = self.collitionRigthSprite(i, distance, salvaguarda=salvaguarda)
            if solucion:
                return solucion
        return False

    def draw(self, surface:pg.surface.Surface):
        if self.direction == -1 and not(self.__aplicado):
            self.image = pg.transform.flip(self.image, True, False)
            self.__aplicado = True
        super().draw(surface)

    def animar(self):
        self.__aplicado = False
        super().animar()