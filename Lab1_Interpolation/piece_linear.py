from __future__ import division  
import numpy as np


class piece_linear : 
    x = [] # 插值点横坐标
    y = [] # 插值点纵坐标
    outcome = [] 

    def __init__(self,x,y) : 
        self.x = x
        self.y = y
        # print(self.x)
    
    def calculation(self,x,left,pace):
        # given the test_set x
        # calculate the outcome
        for i in range(len(x)):
            # print(x[i])
            temp = int((x[i]-left)//pace)
            # print(temp)
            #for every x
            outcome = self.y[temp]*(x[i]-self.x[temp+1])/(self.x[temp]-self.x[temp+1])+self.y[temp+1]*(x[i]-self.x[temp])/(self.x[temp+1]-self.x[temp])
            self.outcome.append(outcome)
        # print(self.outcome)


