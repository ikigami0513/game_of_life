from tkinter import *
from Cellule import Cellule
from Population import Population

class FormScreen:
    __root: Tk

    def __init__(self, root):
        self.__root = root
        self.setupWidget()

    def setupWidget(self):
        dimensionLabel = Label(self.__root, text='Dimension :')
        dimensionLabel.grid(row=0, column=0)

        self.x = Entry(self.__root, width=10)
        self.x.grid(row=1, column=0)

        self.y = Entry(self.__root, width=10)
        self.y.grid(row=1, column=1)

        AnneeLabel = Label(self.__root, text="Nombre d'années : ")
        AnneeLabel.grid(row=2, column=0)

        self.nbAnnee = Entry(self.__root, width=10)
        self.nbAnnee.grid(row=3, column=0)

        self.randomValue = IntVar()
        self.random = Checkbutton(self.__root, text="Random", variable=self.randomValue)
        self.random.grid(row=4, column=0)

        submit = Button(self.__root, text='Commencer', command=self.__start)
        submit.grid(row=5, column=0)

    def __start(self):
        if self.x.get().isdigit() and self.y.get().isdigit() and self.nbAnnee.get().isdigit():
            self.__root.population = Population([[Cellule(i, j, self.__root) for j in range(int(self.y.get()))] for i in range(int(self.x.get()))])
            self.__root.nbAnnee = int(self.nbAnnee.get())
            self.__root.isRandom = self.randomValue.get()
            self.destroy()
            self.__root.start()

    def destroy(self):
        for widget in self.__root.winfo_children():
            widget.destroy()