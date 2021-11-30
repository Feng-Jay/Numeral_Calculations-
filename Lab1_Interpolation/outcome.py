from numpy.lib.function_base import diff, select
from Vandermonde import Vandermonde_Martix
from Lagrange import Lagrange
from Newton import Newton
from piece_linear import piece_linear
from Hermitian import Hermitian
import numpy as np
import math
import random

# 

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
def fx(x,*args):
    arg=args[0]
    # print(arg)
    c = arg[0]
    d = arg[1]
    e = arg[2]
    f = arg[3]

    fx = c * np.sin(d * x) + e * np.cos(f * x)
    # print(fx)
    return fx

def dfx(x,*args):
    arg=args[0]
    # print(arg)
    c = arg[0]
    d = arg[1]
    e = arg[2]
    f = arg[3]

    fx = c*d * np.cos(d * x) - e * f * np.sin(f * x)
    return fx


if __name__ == "__main__":
    array = input("Please input the Interval [a,b]: ")
    a = [float(n) for n in array.split()]
    array = input("Please input the value: c d e f to build the f(x): ")
    args = [float(n) for n in array.split()]
    n = int(input("Please input the value n+1: "))
    m = int(input("Please input the value m for test: "))
    x_set = [] # n+1个插值点
    y_set = [] # 插值点处y值
    dy_set = [] # 导数集合
    test_set = [] #m个检测点
    interval = a[1] - a [0] #输入区间的长度
    pace = interval/(n-1)
    # print(args)
    # print(pace) #步长
    for i in range(n):
        x_set.append(a[0]+i*pace) #给定插值点x
        y_set.append(fx(x_set[i],args))
        dy_set.append(dfx(x_set[i],args))
    # print(y_set)
    # print(x_set)
    # 获得所有插值点
    for i in range(m):
        temp = random.uniform(a[0],a[1])
        test_set.append(temp)
    test_set.sort()
    print("test_case:", test_set)
    # 准备构造插值函数
    standard = []
    for i in range(m):
        standard.append(fx(test_set[i],args))
    print("Standard outcome: ",standard)
    vander=Vandermonde_Martix(n,x_set,y_set)
    vander.calculation()
    vander.function(test_set)
    print("Vandermonde outcome: ", vander.outcome)
    lagrange = Lagrange(x_set, y_set)
    lagrange.calculation(test_set)
    print("Lagrange outcome: ", lagrange.outcome)
    newton = Newton(x_set,y_set,pace)
    newton.calculation(test_set)
    print("Newton outcome: ", newton.outcome)
    y_set1 = y_set
    y_set1.append(fx(a[1],args))
    dy_set.append(dfx(a[1],args))
    # print(y_set1)
    x_set1 = x_set
    # x_set1.insert(0,a[0])
    x_set1.append(a[1])
    piecel = piece_linear(x_set1,y_set1)
    piecel.calculation(test_set,a[0],pace)
    print("PieceLinear outcome: ", piecel.outcome)
    hermitian = Hermitian(x_set1, y_set1)
    hermitian.calculation(dy_set, test_set, a[0], pace)
    print("Hermitian outcome: ", hermitian.outcome)

    # Calculation is done
    # Here is the analyse stage
    print("计算误差分别为: ")
    diff1 = []
    diff_avg1 = 0
    for i in range(m):
        diff1.append(vander.outcome[i]-standard[i])
        diff_avg1 = diff_avg1 + vander.outcome[i]-standard[i]
    diff2 = []
    diff_avg1 = diff_avg1 / m

    diff_avg2 = 0
    for i in range(m):
        diff2.append(lagrange.outcome[i]-standard[i])
        diff_avg2 = diff_avg2 + lagrange.outcome[i]-standard[i]
    diff_avg2 = diff_avg2 / m
    
    diff3 = []
    diff_avg3 = 0
    for i in range(m):
        diff3.append(newton.outcome[i]-standard[i])
        diff_avg3 = diff_avg3 + newton.outcome[i]-standard[i]
    diff_avg3 = diff_avg3 / m
    
    diff_avg4 = 0
    diff4 = []
    for i in range(m):
        diff4.append(piecel.outcome[i]-standard[i])
        diff_avg4 = diff_avg4 + piecel.outcome[i]-standard[i]
    diff_avg4 = diff_avg4 / m

    diff_avg5 = 0
    diff5 = []
    for i in range(m):
        diff5.append(hermitian.outcome[i]-standard[i])
        diff_avg5 = diff_avg5 + hermitian.outcome[i]-standard[i]
    diff_avg5 = diff_avg5 / m
    # print(diff1)
    print("Average = ",diff_avg1)
    # print(diff2)
    print("Average = ",diff_avg2)
    # print(diff3)
    print("Average = ",diff_avg3)
    # print(diff4)
    print("Average = ",diff_avg4)
    # print(diff5)
    print("Average = ",diff_avg5)
# print(a)1
# print(args)

plt.figure(1)
plt.subplot(1,2,1)
plt.plot(test_set, vander.outcome,color='r')
plt.xlabel('插值点横坐标')
plt.ylabel('插值点函数值')
plt.title("范德蒙德多项式插值")
plt.subplot(1,2,2)
plt.plot(test_set, standard, color='b')
plt.xlabel('横坐标')
plt.ylabel('函数值')
plt.title("标准函数fx")

plt.figure(2)
plt.subplot(1,2,1)
plt.plot(test_set, lagrange.outcome,color='r')
plt.xlabel('插值点横坐标')
plt.ylabel('插值点函数值')
plt.title("Lagrange插值")
plt.subplot(1,2,2)
plt.plot(test_set, standard, color='b')
plt.xlabel('横坐标')
plt.ylabel('函数值')
plt.title("标准函数fx")

plt.figure(3)
plt.subplot(1,2,1)
plt.plot(test_set, newton.outcome,color='r')
plt.xlabel('插值点横坐标')
plt.ylabel('插值点函数值')
plt.title("Newton 插值")
plt.subplot(1,2,2)
plt.plot(test_set, standard, color='b')
plt.xlabel('横坐标')
plt.ylabel('函数值')
plt.title("标准函数fx")

plt.figure(4)
plt.subplot(1,2,1)
plt.plot(test_set, piecel.outcome,color='r')
plt.xlabel('插值点横坐标')
plt.ylabel('插值点函数值')
plt.title("分段线性插值")
plt.subplot(1,2,2)
plt.plot(test_set, standard, color='b')
plt.xlabel('横坐标')
plt.ylabel('函数值')
plt.title("标准函数fx")

plt.figure(5)
plt.subplot(1,2,1)
plt.plot(test_set, hermitian.outcome,color='r')
plt.xlabel('插值点横坐标')
plt.ylabel('插值点函数值')
plt.title("分段三次Hermite插值")
plt.subplot(1,2,2)
plt.plot(test_set, standard, color='b')
plt.xlabel('横坐标')
plt.ylabel('函数值')
plt.title("标准函数fx")
plt.show()
