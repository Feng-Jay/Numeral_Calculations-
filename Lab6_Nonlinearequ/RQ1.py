import numpy as np
import math 
from scipy import optimize
from scipy.misc import derivative
import copy

over_flow = 1000

def Fx(x):
    return x**2 - 3*x + 2 - math.exp(x)

def dFx(x):
    return derivative(Fx,x,dx=1e-6)

def Fi(x):
    return (x**2+2-math.exp(x))/3

def dFi(x):
    return derivative(Fi,x,dx=1e-6)

def Gx(x):
    return x**3 + 2 * x**2 + 10 * x - 20

def dGx(x):
    return derivative(Gx,x,dx=1e-6)

def Fig(x):
    return 20/(x**2 + 2*x + 10)

def dFig(x):
    return derivative(Fig,x,dx=1e-6)

def test_convergence_f(x):
    maximum = optimize.fminbound(lambda x: -dFi(x), 0, 1)
    maximum = dFi(maximum)
    minimum = optimize.fminbound(dFi,0,1)
    minimum = dFi(minimum)
    if max(abs(maximum),abs(minimum)) >= 1:
        print("fx不满足局部收敛")
        return 0
    return 1
def test_convergence_g(x):
    maximum = optimize.fminbound(lambda x: -dFig(x), 0, 1)
    minimum = optimize.fminbound(dFig,0,1)
    if max(abs(maximum),abs(minimum)) >= 1:
        print("gx不满足局部收敛")
        return 0
    return 1

def iteration_f(x_0):
    global over_flow
    x_temp = copy.deepcopy(x_0)
    times = 0
    x_k=0
    while True :
        if x_k > over_flow :
            print("无法收敛!")
            # exit()
            return times, x_k
        times += 1
        x_k = Fi(x_temp)
        if abs(x_k - x_temp) < 10e-8:
            break
        x_temp = x_k
        if times > 100:
            break
    return times, x_k

def Iteration_g(x_0):
    x_temp = copy.deepcopy(x_0)
    times = 0
    x_k=0
    global over_flow 
    while True:
        if x_k > over_flow :
            print("无法收敛!")
            return times, x_k
        times += 1
        x_k = Fig(x_temp)
        if abs(x_k - x_temp) < 10e-8:
            break
        x_temp = x_k
        if times > 100:
            break
    return times, x_k

def Sp_Iteration_f(x_0):
    x_temp = copy.deepcopy(x_0)
    times = 0
    x_k=0
    global over_flow
    while True:
        if x_k > over_flow :
            print("无法收敛!")
            return times, x_k
        times +=1
        y = Fi(x_temp)
        z = Fi(y)
        x_k = x_temp - ((y-x_temp)**2/(z-2*y+x_temp))
        if abs(x_k - x_temp) < 10e-8:
            break
        x_temp = x_k
        if times > 100:
            break
    return times,x_k

def Sp_Iteration_g(x_0):
    x_temp = copy.deepcopy(x_0)
    times = 0
    x_k=0
    global over_flow
    while True:
        if x_k > over_flow :
            print("无法收敛!")
            return times, x_k
        times +=1
        y = Fig(x_temp)
        z = Fig(y)
        x_k = x_temp - ((y-x_temp)**2/(z-2*y+x_temp))
        if abs(x_k - x_temp) < 10e-8:
            break
        x_temp = x_k
        if times > 100:
            break
    return times,x_k

def Newton_fi_f(x):
    return x - Fx(x)/dFx(x)

def Newton_fi_g(x):
    return x - Gx(x)/dGx(x)

def Newton_iteration_f(x_0):
    x_temp = copy.deepcopy(x_0)
    times = 0
    x_k = 0
    global over_flow
    while True:
        if x_k > over_flow :
            print("无法收敛!")
            return times, x_k
        times +=1
        x_k = Newton_fi_f(x_temp)
        if abs(x_k - x_temp) < 10e-8:
            break
        x_temp = x_k
        if times > 100:
            break
    return times,x_k

def Newton_iteration_g(x_0):
    x_temp = copy.deepcopy(x_0)
    times = 0
    x_k = 0
    global over_flow
    while True:
        if x_k > over_flow :
            print("无法收敛!")
            return times, x_k
        times +=1
        x_k = Newton_fi_g(x_temp)
        if abs(x_k - x_temp) < 10e-8:
            break
        x_temp = x_k
        if times > 100:
            break
    return times,x_k

if __name__ == "__main__":
    x_0 = 10
    print("迭代初值为: ",x_0)
    flag = test_convergence_f(x_0)
    if flag == 0 :
        exit()
    print("<<----------普通不动点迭代---------->>")
    times, outcome = iteration_f(x_0)
    print("迭代次数: ",times, "方程的解为: ",outcome)

    print("<<----------斯特芬森加速后---------->>")
    times, outcome = Sp_Iteration_f(x_0)
    print("迭代次数: ",times, "方程的解为: ",outcome)

    print("<<----------牛顿迭代法---------->>")
    times, outcome = Newton_iteration_f(x_0)
    print("迭代次数: ",times, "方程的解为: ",outcome)

    ans_f = optimize.fsolve(Fx,x_0)
    print("标准解为: ",ans_f)

    print("<----------g(x)---------->")

    x_0 = 10
    print("迭代初值为: ",x_0)
    flag = test_convergence_g(x_0)
    if flag == 0 :
        exit()
    print("<<----------普通不动点迭代---------->>")
    times_g, outcome_g = Iteration_g(x_0)
    print("迭代次数: ",times_g, "方程的解为: ",outcome_g)

    print("<<------斯特芬森加速后------>>")
    times_g, outcome_g = Sp_Iteration_g(x_0)
    print("迭代次数: ",times_g, "方程的解为: ",outcome_g)
    
    print("<<----------牛顿迭代法---------->>")
    times_g, outcome_g = Newton_iteration_g(x_0)
    print("迭代次数: ",times_g, "方程的解为: ",outcome_g)

    ans_g = optimize.fsolve(Gx,1.1)
    print("标准解为: ",ans_g)