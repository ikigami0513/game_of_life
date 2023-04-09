from tkinter import *
from Cellule import Cellule
from Population import Population

class GameChoiceScreen:
    __root: Tk

    def __init__(self, root):
        self.__root = root

        label = Label(self.__root, text="à coder")
        label.grid(row=0, column=0)