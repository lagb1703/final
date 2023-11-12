class Observer:

    def __init__(self, id):
        self.id = id

    def notify(self):
        pass

class Observable:
    
    def __init__(self):
        self.looking = []
    
    def notifyAll(self):
        for i in self.looking:
            i.notify()

    def addObserver(self, observer:Observer)->None:
        self.looking.append(observer)

    def removeObserver(self, position=-1, id=-1):
        if position != -1:
            if position < len(self.looking):
                del self.looking[position]
            return
        if id != -1:
            position = 0
            for i in self.looking:
                if i.id == id:
                    break
                position += 1
            if position < len(self.looking):
                del self.looking[position]
            return
