import numpy as np
import math 
import copy
from numpy.lib.type_check import real
from sympy import *

def f1(x1,x2,x3):
    return 3*x1 - cos(x2*x3) - 1/2

def df1_1(x):
    return diff(f1(x1,x2,x3),x1).subs({x1: x[0], x2: x[1], x3:x[2]})

def df1_2(x):
    return diff(f1(x1,x2,x3),x2).subs({x1: x[0], x2: x[1], x3:x[2]})

def df1_3(x):
    return diff(f1(x1,x2,x3),x3).subs({x1: x[0], x2: x[1], x3:x[2]})


def f2(x1,x2,x3):
    return x1**2 - 81*(x2+0.1)**2 + sin(x3) +1.06

def df2_1(x):
    return diff(f2(x1,x2,x3),x1).subs({x1: x[0], x2: x[1], x3:x[2]})

def df2_2(x):
    return diff(f2(x1,x2,x3),x2).subs({x1: x[0], x2: x[1], x3:x[2]})

def df2_3(x):
    return diff(f2(x1,x2,x3),x3).subs({x1: x[0], x2: x[1], x3:x[2]})


def f3(x1,x2,x3):
    return exp(-1*x1*x2) + 20*x3 + (10/3)*pi -1

def df3_1(x):
    return diff(f3(x1,x2,x3),x1).subs({x1: x[0], x2: x[1], x3:x[2]})

def df3_2(x):
    return diff(f3(x1,x2,x3),x2).subs({x1: x[0], x2: x[1], x3:x[2]})

def df3_3(x):
    return diff(f3(x1,x2,x3),x3).subs({x1: x[0], x2: x[1], x3:x[2]})


def Newton(x):
    A = np.zeros((3,3),dtype=np.float)
    A_2 = np.zeros((3,1),dtype=np.float)
    B = np.array([1/2,-1.06,1-(10/3)*math.pi]).reshape(-1,1)
    x_temp = copy.deepcopy(x)
    times = 0
    while True:
        times+=1
        # input("")
        # print(x_temp)
        A[0][0] = df1_1(x_temp[0])
        A[0][1] = df1_2(x_temp[0])
        A[0][2] = df1_3(x_temp[0])
        A[1][0] = df2_1(x_temp[0])
        A[1][1] = df2_2(x_temp[0])
        A[1][2] = df2_3(x_temp[0])
        A[2][0] = df3_1(x_temp[0])
        A[2][1] = df3_2(x_temp[0])
        A[2][2] = df3_3(x_temp[0])
        A_2[0][0] = f1(x_temp[0][0],x_temp[0][1],x_temp[0][2])
        A_2[1][0] = f2(x_temp[0][0],x_temp[0][1],x_temp[0][2])
        A_2[2][0] = f3(x_temp[0][0],x_temp[0][1],x_temp[0][2])
        # print(A)
        A_reverse = np.linalg.inv(A)
        # print(A_reverse)
        # print(np.dot(A_reverse,A_2))
        x_1 = x_temp.T -  np.dot(A_reverse,A_2)
        # print(x_1)
        # print(x_1)
        if np.linalg.norm(np.abs(x_1-x_temp.T),ord=np.inf) < 10e-8:
            return times, x_temp
        x_temp = x_1.T
        # break

def fix_f1(x1,x2,x3):
    return math.cos(x2*x3)/3 + 1/6
def fix_f2(x1,x2,x3):
    return sqrt(x1**2 + math.sin(x3) +1.06)/9 - 0.1
def fix_f3(x1,x2,x3):
    return 1/20 - math.pi/6 - math.exp(-1*x1*x2)/20

def Fixed(x):
    x_temp = copy.deepcopy(x)
    x_temp = x_temp[0]
    times = 0
    x_k = [0,0,0]
    # print(x_temp)
    while True:
        times+=1
        x_k[0] = fix_f1(x_temp[0],x_temp[1],x_temp[2])
        x_k[1] = fix_f2(x_temp[0],x_temp[1],x_temp[2])
        x_k[2] = fix_f3(x_temp[0],x_temp[1],x_temp[2])
        # print(x_k[:])
        # print(x_k-x_temp)
        if np.linalg.norm(np.abs(x_k-x_temp),ord=np.inf) < 10e-8:
            return times, x_k
        x_temp[:] = x_k[:]
        if times > 1000:
            print("无法收敛")
            return times, x_k






if __name__ == "__main__":
    x1, x2, x3 = symbols('x1 x2 x3', real=True)

    x_0 = np.zeros((1,3),dtype=float)
    x_0=np.array([[5,5,5]])
    print("初始迭代值: ", x_0)
    print("<<--------不动点迭代法-------->>")
    times, outcome = Fixed(x_0)
    print("迭代次数: ",times, "方程的解为: ",outcome)
    print("<<--------牛顿迭代法-------->>")
    x_0 = np.array([[[0,0,0]],[[5,5,5]],[[1,1,1]]])
    for i in range(0,3):
        times, outcome = Newton(x_0[i])
        print("初值为",x_0[i])
        print("迭代次数: ",times, "方程的解为: ",outcome)
