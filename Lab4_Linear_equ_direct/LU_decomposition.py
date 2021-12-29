import numpy as np
import copy
np.set_printoptions(threshold=np.inf)
A = np.array([
    [30,33,-43,-11,-38,-29,37,28,23],
    [-480,-523,644,128,621,480,-618,-489,-329],
    [60,266,-1862,-1991,464,546,-968,-1567,1652],
    [540,624,-782,290,-893,123,567,5,-122],
    [-450,-675,2245,2326,-1512,1230,-822,129,-189],
    [-300,-120,-1114,-1295,1946,302,-376,-1540,-609],
    [1080,998,508,2460,-1628,-1358,2896,2828,-2002],
    [-1080,-1408,3340,2267,21,-1202,866,-2690,-1351],
    [-300,-435,1594,1685,340,2279,-27,2917,-2336]
])

B = np.array([188,-3145,-4994,680,7845,1876,9712,-11599,10127]).reshape((-1,1))

def Lu_decomposition(A,B):
    X = np.zeros((len(A),1))
    Y = np.zeros((len(A),1))
    for i in range(len(A)):
        if i == 0 :
            if A[i][i] == 0 :
                print("ERROR! This function can not solved by this method!")
                return 
            for j in range(1,len(A)):
                A[j][i] = A[j][i] / A[i][i]
            Y[i] = B[i]
            continue
        temp = 0
        for m in range(i):
            temp += A[i][m]* A[m][i]
        A[i][i] = A[i][i] - temp
        if A[i][i] == 0 :
            print("ERROR! This function can not solved by this method!")
            return
        for j in range(i+1,len(A)):
            temp = 0
            temp2 =0
            for k in range(0,i): 
                temp += A[i][k] * A[k][j]
                temp2 += A[j][k] * A[k][i]
            # 求uij
            A[i][j] = A[i][j] - temp
            #求lji 
            A[j][i] = (A[j][i] - temp2)/A[i][i]
        temp2 = 0
        for j in range(0,i):
            temp2 += A[i][j] * Y[j]
        Y[i] = B[i] - temp2
    # print(A)
    # print(Y)
    # 回代法求解 UX=Y
    for i in range(len(A)-1,-1,-1):
        if i == len(A) -1 :
            X[i] = Y[i] / A[i][i]
            continue
        temp = 0
        for j in range(i+1,len(A)):
            temp += A[i][j] * X[j]
        X[i] = (Y[i] - temp)/A[i][i]
    return X


if __name__ == "__main__":
    # print(A)
    # print(B)
    # test = np.array([
    #     [1,2,3,4],
    #     [2,9,12,15],
    #     [3,26,41,49],
    #     [5,40,107,135]
    # ])
    # test_b = np.array([1,2,3,4]).reshape((-1,1))
    # outcome = Lu_decomposition(test,test_b)
    ans = np.linalg.solve(A,B)
    ans = ans.T
    print("标准答案为:")
    print(ans)
    outcome = Lu_decomposition(A,B)
    outcome = outcome.T
    print("LU分解法结果为: ")
    print(outcome)
    print("L矩阵为")
    L = copy.copy(A)
    for i in range(len(A)):
        for j in range(len(A)):
            if j == i :
                L[i][j] = 1
                continue
            if j >i :
                L[i][j] = 0
    print(L)
    print("U矩阵为")
    U = copy.copy(A)
    for i in range(len(A)):
        for j in range(len(A)):
            if j <i :
                U[i][j] = 0
    print(U)




    print("---------------------随机矩阵检测--------------------")
    ran_mar = np.random.rand(50,50)*100 
    ran_b = np.random.rand(50,1)*100
    # print(ran_mar)
    # print(ran_b)
    ans2 = np.linalg.solve(ran_mar,ran_b).T
    print("标准答案为:")    
    print(ans2)

    outcome2 = Lu_decomposition(ran_mar,ran_b)
    outcome2 = outcome2.T
    print("LU分解法结果为: ")
    print(outcome2)
    print("L矩阵为")
    L = copy.copy(ran_mar)
    for i in range(len(ran_mar)):
        for j in range(len(ran_mar)):
            if j == i :
                L[i][j] = 1
                continue
            if j >i :
                L[i][j] = 0
    print(L)
    print("U矩阵为")
    U = copy.copy(ran_mar)
    for i in range(len(ran_mar)):
        for j in range(len(ran_mar)):
            if j <i :
                U[i][j] = 0
    print(U)
# Log parser                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               