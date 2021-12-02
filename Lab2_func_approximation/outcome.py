import numpy as np
import random

def fx(c, x):
    y = []
    for i in range(len(x)):
        temp = 1/(1+c*x[i]**2)
        y.append(temp)
    return y



if __name__ == "__main__":

    temp = input("Please input the Approximation Internal [a,b]: ")
    a = [float(n) for n in temp.split()]
    c = float(input("Please the paramester c of f(x): "))
    k = int(input("Please input the k exp of approximation's function: "))
    n = int(input("Please input the Sampling numbers n+1: "))
    m = int(input("Please input the test_set numbers m: "))

    pace = (a[1] - a[0])/n

    x = []
    for i in range(n):
        x.append(a[0]+i*pace) 
    
    test_set = []
    for i in range(m):
        temp = random.uniform(a[0],a[1])
        test_set.append(temp)
    test_set.sort()
    print("test_case:", test_set)
    standard = []
    standard = fx(c,test_set)
    print("Standard outcome: ",standard)