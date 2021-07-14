import math
import matplotlib.pyplot as plt

colNum = 0
class collatz:
    def main():
        colNum = int(input('Please input number for collatz: '))
        colPoints = []
        colPoints.append(colNum)
        while colNum != 1:
            if colNum % 2 == 0:
                colNum = colNum / 2
                print(colNum)
                colPoints.append(colNum)
                continue
            if colNum % 2 == 1:
                colNum = 3*colNum + 1
                print(colNum)
                colPoints.append(colNum)
                continue

        plt.polar(colPoints)
        plt.show()
        
        plt.plot(colPoints)
        plt.show()






    main()
