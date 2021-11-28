import numpy as np

class Vandermonde_Martix : 
    martix=[]
    def __init__(self, xn, *x):
        x_set = x[0]
        # print(x_set)
        self.martix=[[x_set[j]**i for i in range(xn)] for j in range(xn)]
        print(self.martix)

