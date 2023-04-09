from tkinter import *
import time

class GameScreen:
    __root: Tk

    def __init__(self, root):
        self.__root = root
        self.setupWidget()
        self.game()

    def game(self):
        for i in range(self.__root.nbAnnee):
            self.__root.population.update()
            self.__root.update_idletasks()
            time.sleep(3)

    def setupWidget(self):
        for i in range(len(self.__root.population.matrice)):
            for j in range(len(self.__root.population.matrice)):
                self.__root.population.matrice[i][j].setupTexture()