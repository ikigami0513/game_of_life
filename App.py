from tkinter import *
from Population import Population
from Cellule import Cellule
from Screen.FormScreen import FormScreen
from Screen.GameScreen import GameScreen
from Screen.GameChoiceScreen import GameChoiceScreen

class App(Tk):
    population: Population
    nbAnnee: int
    isRandom: bool

    def __init__(self):
        super().__init__()
        FormScreen(self)

    def start(self):
        if self.isRandom:
            GameScreen(self)
        else:
            GameChoiceScreen(self)

    