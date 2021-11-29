from Vandermonde import Vandermonde_Martix
import numpy as np
import math
import random


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



if __name__ == "__main__":
    array = input("Please input the Interval [a,b]: ")
    a = [float(n) for n in array.split()]
    array = input("Please input the value: c d e f to build the f(x): ")
    args = [float(n) for n in array.split()]
    n = int(input("Please input the value n+1: "))
    m = int(input("Please input the value m for test: "))
    x_set = [] # n+1个插值点
    y_set = [] # 插值点处y值
    test_set = [] #m个检测点
    interval = a[1] - a [0] #输入区间的长度
    pace = interval/n
    # print(args)
    # print(pace) #步长
    for i in range(n):
        x_set.append(a[0]+i*pace) #给定插值点x
        y_set.append(fx(x_set[i],args))
    # print(y_set)
    # print(x_set)
    # 获得所有插值点
    for i in range(m):
        temp = random.uniform(a[0],a[1])
        test_set.append(temp)
    # 准备构造插值函数
    vander=Vandermonde_Martix(n,x_set,y_set)
    print("cal")
    vander.calculation()
    outcome1 = vander.function(test_set)
    print("outcome1:\n",outcome1)
    standard = []
    for i in range(m):
        standard.append(fx(test_set[i],args))
    print("fx=\n",standard)

# print(a)
# print(args)