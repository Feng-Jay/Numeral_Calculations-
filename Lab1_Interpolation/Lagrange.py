import numpy as np

class Lagrange :
    x = [] # 存放插值点坐标值
    y = [] # 存放插值点函数值
    denominator = [] # Lagrange function's Deno...
    outcome = []
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        for i in range(len(x)):
            temp = 1
            for j in range(len(x)):
                if i == j : 
                    continue
                temp = temp * (x[i]-x[j])
            self.denominator.append(temp)
        # Store all the denominators' value
        # print(self.denominator)
    
    def calculation(self, x):
        # Input the test set x
        for i in range(len(x)): 
            # for every x elem
            outcome = 0
            for j in range(len(self.x)):
                temp = 1
                for k in range(len(self.x)):
                    if k == j :
                        continue
                    temp = temp * (x[i]-self.x[k]) 
                outcome = outcome + self.y[j] * (temp/self.denominator[j])
            self.outcome.append(outcome)
        print(self.outcome)