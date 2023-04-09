class Population:
    matrice: list

    def __init__(self, matrice):
        self.matrice = matrice

    def __getNeighborOfCellule(self, i, j):
        neighborCellules = 0
        for n in [-1, 0, 1]:
            for m in [-1, 0, 1]:
                if self.matrice[(i-n)%len(self.matrice)][(j-m)%len(self.matrice[i])].isLife():
                    neighborCellules += 1

        return neighborCellules

    def update(self):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if not self.matrice[i][j].isLife():
                    if self.__getNeighborOfCellule(i, j) == 3:
                        self.matrice[i][j].setIsLife(True)

                else:
                    neighborCellules = self.__getNeighborOfCellule(i, j)
                    if neighborCellules == 2 or neighborCellules == 3:
                        pass
                    else:
                        self.matrice[i][j].setIsLife(False)

                self.matrice[i][j].update()

    def toString(self):
        all_row = ""
        for i in range(len(self.matrice)):
            row = ""
            for j in range(len(self.matrice[i])):
                row += self.matrice[i][j].toString()
            
            all_row += row + "\n"

        return all_row
