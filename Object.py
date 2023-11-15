import pygame.surface as surface
import pygame as pg
import copy

class Objects(pg.sprite.Group):

    def __init__(self, Name):
        super().__init__()
        self.groupName = Name


class Object(pg.sprite.Sprite):

    def __init__(self, id, resolution:tuple, animations,initialPosition = (0,0), initialSprite="initial"):
        super().__init__()
        self.id = id
        self.__animations = animations
        self.resolution = resolution
        # self.image = surface.Surface(resolution)
        # self.image.fill((0,0,0,0))
        # image = pg.transform.scale(animations[initialSprite][0][0], resolution)
        # self.image.blit(image, (0,0))
        # self.image.blit(animations[initialSprite][0][0], (resolution[0]//2, resolution[1]//2))
        self.image = pg.transform.scale(animations[initialSprite][0][0], resolution)
        self.rect = self.image.get_rect()
        self.rect.x = initialPosition[0]
        self.rect.y = initialPosition[1]
        self.__frame = 0
        self.__animationName = initialSprite

    def draw(self, surface:pg.surface.Surface):
        surface.blit(self.image, self.rect)

    def getAnimationName(self):
        return self.__animationName

    def setAnimationName(self, animation:str):
        self.__frame = 0
        self.__animationName = animation

    def setFrame(self, cantidad:int):
        self.__frame = cantidad

    def getFrame(self):
        return self.__frame
    
    def animar(self):
        if self.getAnimationFrameMax() <= 0:
            return
        self.__frame += 1
        if len(self.__animations[self.__animationName][0]) <= self.__frame:
            self.__frame = 0
        imagen = pg.transform.scale(self.__animations[self.__animationName][0][self.__frame], self.resolution)
        self.image = imagen

    def getAnimationFrameMax(self):
        return self.__animations[self.__animationName][1]

    def update(self, colector=None):
        pass