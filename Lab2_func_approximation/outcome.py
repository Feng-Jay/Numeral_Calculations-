from operator import le
import numpy as np
import random
from Legendre import Legendre
from least_square import Square
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

def fx(c, x):
    # x为输入数据数组
    y = []
    for i in range(len(x)):
        temp = 1/(1+c*(x[i]**2))
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
    y = fx(c,x)
         
    test_set = []
    test_set1 = []
    for i in range(m): #普通的测试集合
        temp = random.uniform(a[0],a[1])
        test_set.append(temp)
        
    test_set.sort()
    for i in range(m): #映射的测试集合
        temp = test_set[i]
        test_set1.append((1/(a[1]-a[0]))*(2*temp-a[0]-a[1]))
    
    standard = []
    standard = fx(c,test_set) #原函数测试集对应结果

    legend = Legendre(a)
    legend.calculation(k,c)
    outcome1 = legend.cal_test(test_set1)#计算结果

    lsquare = Square(x,y)
    lsquare.calculation(k) #计算系数
    outcome2 = lsquare.outcome(test_set) #计算结果

    
    outcome_1lll = 0
    for i in range(m):
        outcome_1lll += abs(outcome1[i] - standard[i])
    outcome_1lll = outcome_1lll/m
    print("最佳平方逼近的平均误差为: ",outcome_1lll)

    outcome_2 = 0
    for i in range(m):
        outcome_2 += abs(outcome2[i] - standard[i])
    outcome_2 = outcome_2/m
    print("最小二乘法的平均误差为: ", outcome_2)



    plt.figure(1)
    plt.subplot(1,2,1)
    plt.plot(test_set, outcome1,color='r')
    plt.xlabel('横坐标')
    plt.ylabel('函数值')
    plt.title('最佳平方逼近 k=%i' %k)
    plt.subplot(1,2,2)
    plt.plot(test_set, standard, color='b')
    plt.xlabel('横坐标')
    plt.ylabel('函数值')
    plt.title("标准函数fx")


    plt.figure(2)
    plt.subplot(1,2,1)
    plt.plot(test_set, outcome2,color='r')
    plt.xlabel('横坐标')
    plt.ylabel('函数值')
    plt.title('最小二乘法 k=%i' %k)
    plt.subplot(1,2,2)
    plt.plot(test_set, standard, color='b')
    plt.xlabel('横坐标')
    plt.ylabel('函数值')
    plt.title("标准函数fx")
    plt.show()
