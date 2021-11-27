from Vandermonde import Vandermonde_Martix
import numpy as np
import math

array = input("Please input the Interval [a,b]: ")
a = [float(n) for n in array.split()]
array = input("Please input the value: c d e f to build the f(x): ")
args = [float(n) for n in array.split()]
n = int(input("Please input the value n+1: "))
m = int(input("Please input the value m for test: "))


c = args[0]
d = args[1]
e = args[2]
f = args[3]
x = math.pi/2

fx = c * np.sin(d * x) + e * np.cos(f * x)
print(fx)
# print(a)
# print(args)