from Vandermonde import Vandermonde_Martix
from Lagrange import Lagrange
from Newton import Newton
from piece_linear import piece_linear
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
    standard = []
    for i in range(m):
        standard.append(fx(test_set[i],args))
    print("fx=\n",standard)
    # vander=Vandermonde_Martix(n,x_set,y_set)
    # print("cal")
    # vander.calculation()
    # outcome1 = vander.function(test_set)
    # print("outcome1:\n",outcome1)
    # lagrange = Lagrange(x_set, y_set)
    # lagrange.calculation(test_set)
    # newton = Newton(x_set,y_set,pace)
    # newton.calculation(test_set)
    y_set1 = y_set
    y_set1.append(fx(a[1],args))
    # print(y_set1)
    x_set1 = x_set
    # x_set1.insert(0,a[0])
    x_set1.append(a[1])
    piecel = piece_linear(x_set1,y_set1)
    piecel.calculation(test_set,a[0],pace)
# print(a)1
# print(args)