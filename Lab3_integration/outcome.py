import numpy as np
import math
from scipy import integrate
from trapezoid import T
from romberg import romberg

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

def fx(x):
    # x为输入数据集合
    y = []
    for i in range(len(x)):
        temp = math.sqrt(x[i]) * math.log(x[i])
        y.append(temp)
    return y

def fx1(x):
    # x为输入数据集合
    temp = math.sqrt(x) * math.log(x)
    return temp

if __name__ == "__main__":
    temp = input("Please input the Integration Internal [a,b]: ")
    a = [float(n) for n in temp.split()]
    h = float(input("Please input the pace h: "))
    constrain = float(input("Please input the Accuracy Demand: "))

    outcome, err = integrate.quad(fx1,a[0], a[1])
    print("积分结果为: ",outcome)

    x = []
    temp = 0
    i = 0
    # 给出初始的x集合
    while temp + h <= a[1] :
        temp = a[0] + i*h
        x.append(temp)
        i+=1
    # 给出初始的函数值集合
    y = fx(x)

    # 初始化结束，开始进行复合求积过程
    t = T(outcome,h,a,x,y,constrain)
    t.calculation()

    romberg1 =  romberg(outcome,h,a,x,y,constrain)
    romberg1.calculation()
    
