from Object import Object
class Camera:

    def __init__(self, x, y, resolution:tuple, follow:Object=None,axiesFollow=(True, True)):
        self.x = x
        self.y = y
        self.resolution = resolution
        self.__follow:Object = follow
        self.__axies = axiesFollow

    def update(self):
        if self.__follow:
            if self.__axies[0]:
                self.x = self.__follow.rect.x 
            if self.__axies[1]:
                self.y = self.__follow.rect.y