import numpy as np
import copy

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
    for times in range(0,K):
        for i in range(0,len(A)):
            temp_1 = 0
            for x_i in range(0,i):
                temp_1 += X1[x_i] * A[i][x_i]
            temp_2 = 0
            for x_i in range(i,len(A)):
                temp_2 +=X_temp[x_i] * A[i][x_i]
            X1[i] = X_temp[i] + W*(B[i] - temp_1 -temp_2)/A[i][i]
        count = X1 - X_temp
        cout = max(np.maximum(count, -count))
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

    # w = float(input("Please input the omiga: "))
    w =0
    steps = []
    outcome = []
    for i in range(1,100):
        w = i/50
        # print(w)
        times, outcome_x,count = Sor(X_0,K,E,w)
        # print(X_0)
        steps.append(times)
        outcome.append(outcome_x)
        # print(count)
    min_step = min(steps)
    print(steps)
    print(min_step)
    index = steps.index(min_step)
    print("w = ", index/50)
    print(outcome[index])
        # print("diff = ",count)
        # print("Times={ti}, X=\n {x}".format(ti=times, x=outcome_x))

    Answer = np.linalg.solve(A,B)
    print("Answer is :\n",Answer)
