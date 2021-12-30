import numpy as np
import copy

from numpy.lib.index_tricks import diag_indices

A = np.array([
    [31,-13,0,0,0,-10,0,0,0],
    [-13,35,-9,0,-11,0,0,0,0],
    [0,-9,31,-10,0,0,0,0,0],
    [0,0,-10,79,-30,0,0,0,-9],
    [0,0,0,-30,57,-7,0,-5,0],
    [0,0,0,0,-7,47,-30,0,0],
    [0,0,0,0,0,-30,41,0,0],
    [0,0,0,0,-5,0,0,27,-2],
    [0,0,0,-9,0,0,0,-2,29]
],dtype=np.float)

B = np.array([-15,27,-23,0,-20,12,-7,7,10],dtype=np.float).reshape(-1,1)

def Sor(X,K,E,W):
    global A,B
    X_temp = copy.deepcopy(X)
    # print(X_temp)
    X1 = np.array([0,0,0,0,0,0,0,0,0],dtype=np.float).reshape(-1,1)
    for times in range(1,K+1):
        for i in range(0,len(A)):
            temp_1 = 0
            for x_i in range(0,i):
                temp_1 += X1[x_i] * A[i][x_i]
            temp_2 = 0
            for x_i in range(i,len(A)):
                temp_2 +=X_temp[x_i] * A[i][x_i]
            X1[i] = X_temp[i] + W*(B[i] - temp_1 -temp_2)/A[i][i]
        count = X1 - X_temp
        cout = np.linalg.norm(np.abs(count),ord=np.inf)
        # print(cout)
        if cout < E:
            return times,X1,cout
        X_temp[0:len(A)] = X1[0:len(A)]
    print("Out of Max iteration times!")
    return times,X1,cout


if __name__ == "__main__":
    # print(A)
    # print(B)
    X_temp = input("Please input the initial X(vector): ")
    X_0 = [float(n) for n in X_temp.split()]
    X_0 = np.array(X_0).reshape(-1,1)
    # print(X_0)
    K_temp = input("Please input the Max iteration times K: ")
    K = int(K_temp)
    # print(K)
    E_temp = input("Please input the differ ϵ(Epsilon): ")
    E = float(E_temp)

    w = float(input("Please input the omiga: "))
    print("")
    times, outcome_x,count = Sor(X_0,K,E,w)

    print("迭代次数: {tim}".format(tim=times))
    print("无穷范数为: {co}".format(co=count))
    print("解X= \n",outcome_x.T)

    print("<----------寻找最优w------------>")

    w =0
    steps = []
    outcome = []
    diff = []
    for i in range(1,100):
        w = i/50
        # print(w)
        times, outcome_x,count = Sor(X_0,K,E,w)
        # print(X_0)
        steps.append(times)
        outcome.append(outcome_x)
        diff.append(count)
        # print(count)
    index = np.where(steps == np.min(steps))

    index = index[0]
    min_diff = 1
    min_index = 0
    for item in index:
        if min_diff > diff[item]:
            min_index = item
            min_diff = diff[item]
    
    # print(min_index)
    # print("w = ", index/50)
    print(steps)
    print("所需最少迭代次数为: ")
    print(steps[min_index])
    print("最佳的w选值为: ", (min_index+1)/50)
    print("无穷范数为:",min_diff)
    print("解X为: ")
    print(outcome[min_index].T)

    Answer = np.linalg.solve(A,B)
    print("标准解X :\n",Answer.T)
