class Population:
    __matrice: list

    def __init__(self, matrice):
        self.__matrice = matrice

    def __getNeighborOfCellule(self, i, j):
        neighborCellules = 0
        for n in [-1, 0, 1]:
            for m in [-1, 0, 1]:
                if self.__matrice[(i-n)%len(self.__matrice)][(j-m)%len(self.__matrice[i])].isLife():
                    neighborCellules += 1

        return neighborCellules

    def update(self):
        for i in range(len(self.__matrice)):
            for j in range(len(self.__matrice[i])):
                if not self.__matrice[i][j].isLife():
                    if self.__getNeighborOfCellule(i, j) == 3:
                        self.__matrice[i][j].setIsLife(True)

                else:
                    neighborCellules = self.__getNeighborOfCellule(i, j)
                    if neighborCellules == 2 or neighborCellules == 3:
                        pass
                    else:
                        self.__matrice[i][j].setIsLife(False)

    def toString(self):
        all_row = ""
        for i in range(len(self.__matrice)):
            row = ""
            for j in range(len(self.__matrice[i])):
                row += self.__matrice[i][j].toString()
            
            all_row += row + "\n"

        return all_row
