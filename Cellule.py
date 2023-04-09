import enum
import random
from tkinter import *

class Cellule:
    class State(enum):
        RUNTIME = 'runtime'
        FORM = 'form'

    __state: State

    __isLife: bool
    __status: list = [True, False]
    __statusDict: dict = {
        True: 1,
        False: 0
    }
    __colorDict: dict = {
        True: "#008000",
        False: "#F0F0F2"
    }

    __root: Tk
    __texture: Button

    i: int
    j: int

    def __init__(self, i, j, root, isLife=None):
        if isLife == None:
            self.__isLife = self.__status[random.randint(0,1)]
        else:
            self.__isLife = isLife

        self.__root = root
        self.i = i
        self.j = j

    def setupTexture(self):
        self.__texture = Button(self.__root, text="", state="disabled", width=5, height=3, bg=self.__colorDict[self.__isLife])
        self.__texture.grid(row=self.i, column=self.j)

    def isLife(self):
        return self.__isLife
    
    def setIsLife(self, isLife):
        self.__isLife = isLife

    def toString(self):
        return str(self.__statusDict[self.__isLife])
    
    def update(self):
        self.__texture.configure(bg=self.__colorDict[self.__isLife])