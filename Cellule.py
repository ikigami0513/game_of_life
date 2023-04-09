import random

class Cellule:
    __isLife: bool
    __status: list = [True, False]
    __statusDict: dict = {
        True: 1,
        False: 0
    }

    def __init__(self, isLife=None):
        if isLife == None:
            self.__isLife = self.__status[random.randint(0,1)]
        else:
            self.__isLife = isLife

    def isLife(self):
        return self.__isLife
    
    def setIsLife(self, isLife):
        self.__isLife = isLife

    def toString(self):
        return str(self.__statusDict[self.__isLife])