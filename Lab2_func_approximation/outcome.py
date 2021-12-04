from operator import le
import numpy as np
import random
from Legendre import Legendre
from sympy.functions.special.polynomials import legendre
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

def fx(c, x):
    # x为输入数据数组
    y = []
    for i in range(len(x)):
        temp = 1/(1+c*x[i]**2)
        y.append(temp)
    return y



if __name__ == "__main__":

    temp = input("Please input the Approximation Internal [a,b]: ")
    a = [float(n) for n in temp.split()]
    c = float(input("Please the paramester c of f(x): "))
    k = int(input("Please input the k exp (k=1|2|3): "))
    n = int(input("Please input the Sampling numbers n+1: "))
    m = int(input("Please input the test_set numbers m: "))

    pace = (a[1] - a[0])/n

    x = []
    for i in range(n):
        x.append(a[0]+i*pace) 
    
    test_set = []
    test_set1 = []
    for i in range(m):
        temp = random.uniform(a[0],a[1])
        test_set.append(temp)
    test_set.sort()
    for i in range(m):
        temp = test_set[i]
        test_set1.append((1/(a[1]-a[0]))*(temp*2-a[0]-a[1]))
    # print("test_case1:", test_set1)
    
    standard = []
    standard = fx(c,test_set)

    legend = Legendre(a)
    legend.calculation(k,c)
    print(legend.coeffi)
    outcome1 = legend.cal_test(test_set1, k)
    # print(outcome1)




    
    outcome = 0
    for i in range(m):
        outcome = outcome + abs(outcome1[i] - standard[i])
    outcome = outcome/m
    print("平均误差为: ", outcome)



    plt.figure(1)
    plt.subplot(1,2,1)
    plt.plot(test_set, outcome1,color='r')
    plt.xlabel('逼近函数横坐标')
    plt.ylabel('逼近函数值')
    plt.title("逼近函数")
    plt.subplot(1,2,2)
    plt.plot(test_set, standard, color='b')
    plt.xlabel('横坐标')
    plt.ylabel('函数值')
    plt.title("标准函数fx")

    plt.show()
