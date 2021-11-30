from __future__ import division  
import numpy as np

class Hermitian :
    x = [] # 插值点横坐标
    y = [] # 插值点纵坐标
    outcome = []

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calculation(self, d_set, x, left, pace):
        for i in range(len(x)):
            temp = int((x[i]-left)//pace)
            outcome = ((x[i]-self.x[temp+1])/(self.x[temp]-self.x[temp+1]))**2 * ( 1 + ( 2 * (x[i]-self.x[temp]) / (self.x[temp+1]-self.x[temp]) )) * self.y[temp]\
                      + 