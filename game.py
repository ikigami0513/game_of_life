from Cellule import Cellule
from Population import Population
import os
import time

def main():
    population = Population([[Cellule() for j in range(10)] for i in range(10)])

    os.system('cls')
    print(f"année 0")
    print(population.toString())
    time.sleep(3)
    os.system('cls')

    for i in range(1, 10):
        population.update()
        print(f"année {i}")
        print(population.toString())
        time.sleep(3)
        os.system('cls')

if __name__ == '__main__':
    main()