from Observables import Observer
class Alarm(Observer):

    def __init__(self, time:int, interval:int, repeat:bool, funtion):
        super().__init__(time)
        self.__finalTime = time + interval
        self.interval = interval
        self.__repeat = repeat
        self.__funtion = funtion

    def notify(self, time):
        self.__funtion()
        if self.__repeat:
            self.__finalTime = time + self.interval

    def destroy(self):
        self.__repeat = False

    def isRepeat(self):
        return self.__repeat

    def isTime(self, time):
        return time >= self.__finalTime
    
    #testing