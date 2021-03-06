import numpy as np

class Vandermonde_Martix : 
    martix=[]
    xn = 0
    x = []
    y = []
    A = []
    outcome = []
    def __init__(self, xn, x, y):
        # print(x)
        # print(y)
        # print(x_set)
        self.x = x
        self.y = y
        self.xn = xn
        self.martix=[[x[j]**i for i in range(xn)] for j in range(xn)]
        # print("martix:\n",self.martix)
        # print("xn = ",self.xn)
        # print('x: \n', self.x)
        # print("y: \n", self.y)
    def calculation(self):
        # print("self.martix: \n",self.martix)
        coefficient = np.array(self.martix)
        # print("coefficient: \n",coefficient)
        # a = np.array([[1, 2], [3, 5]]) 
        # print("a:\n",a)
        # print("self's y: \n",self.y)
        y = np.array(self.y)
        #print("y: \n", y)
        self.A = np.linalg.solve(coefficient,y)
        # print(self.A)

    def function(self,x):
        # x is the set of test dots.
        for i in range(len(x)):
            # for each test value
            outcome = 0
            for j in range(self.xn):
                # 这里是每个函数值
                outcome = outcome + self.A[j]*(x[i]**j)
            self.outcome.append(outcome)

