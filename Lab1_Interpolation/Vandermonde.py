import numpy as np

class Vandermonde_Martix : 
    martix=[]
    def __init__(self, xn, x, y):
        print(x)
        print(y)
        # print(x_set)
        self.martix=[[x[j]**i for i in range(xn)] for j in range(xn)]
        print(self.martix)

