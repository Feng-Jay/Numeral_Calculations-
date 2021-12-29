import numpy as np

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

def Guass(X,K,E):
    global A,B
    X1 = np.array([0,0,0,0,0,0,0,0,0],dtype=np.float).reshape(-1,1)
    for times in range(0,K):
        for i in range(0,len(A)):
            temp_1 = 0
            for x_i in range(0,i):
                temp_1 += X1[x_i] * A[i][x_i]
            temp_2 = 0
            for x_i in range(i+1,len(A)):
                temp_2 +=X[x_i] * A[i][x_i]
            X1[i] = (B[i] - temp_1 -temp_2)/A[i][i]
        count = X1 - X
        cout = max(np.maximum(count, -count))
        # print(cout)
        if cout < E:
            return times,X1,cout
        X[0:len(A)] = X1[0:len(A)]
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

    times, outcome_x,count = Guass(X_0,K,E)
    print("diff = ",count)
    print("Times={ti}, X=\n {x}".format(ti=times, x=outcome_x))

    Answer = np.linalg.solve(A,B)
    print("Answer is :\n",Answer)
