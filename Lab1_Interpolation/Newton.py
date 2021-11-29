import numpy as np
from numpy.lib.function_base import select

class Newton :
    x = [] # 插值点横坐标
    y = [] # 插值点纵坐标
    martix = [] # 均差矩阵
    outcome = [] 
    def __init__(self,x,y,pace):
        self.x = x
        self.y = y
        self.martix = np.zeros((len(x),len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                if j < i : continue
                if i == 0:
                    self.martix[i][j] = self.y[j]
                else:
                    self.martix[i][j] = (self.martix[i-1][j] - self.martix[i-1][j-1])/(i*pace)
        # print(self.martix)

    def calculation(self,x):
        # x is the set of test values
        for i in range(len(x)):
            # for every test x
            outcome = 0
            for j in range(len(self.x)):
                # calculate n time
                temp = 1
                for k in range(j):
                    if j == 0: break
                    temp =temp * (x[i]- self.x[k])
                outcome = outcome + temp * self.martix[j][j]
            self.outcome.append(outcome)
        
        print(self.outcome)


        