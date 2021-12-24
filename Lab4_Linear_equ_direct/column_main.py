import numpy as np
from numpy import testing
np.set_printoptions(threshold=np.inf)
# Init the martix & Vector
A = np.array([[31,-13,0,0,0,-10,0,0,0],
             [-13,35,-9,0,-11,0,0,0,0],
             [0,-9,31,-10,0,0,0,0,0],
             [0,0,-10,79,-30,0,0,0,-9],
             [0,0,0,-30,57,-7,0,-5,0],
             [0,0,0,0,-7,47,-30,0,0],
             [0,0,0,0,0,-30,41,0,0],
             [0,0,0,0,-5,0,0,27,-2],
             [0,0,0,-9,0,0,0,-2,29]],dtype = float)

B = np.array([-15,27,-23,0,-20,12,-7,7,10],dtype = float).reshape((-1,1))

def column_main_solution(A,B):
    X=np.zeros((len(A),1))
    # print(X)
    # print(len(A))
    for k in range(len(A)-1):
        # print(A[k:len(A),k])
        temp = A[k:len(A),k]
        temp = np.maximum(temp, -temp)
        # print(temp)
        j = np.argmax(temp)
        if A[k+j][k] == 0 : 
            print("ERROR! This equation set can not solved by this method!")
            return
        # print(j)
        tmp = np.copy(A[k+j])
        A[k+j] = A[k]
        A[k] = tmp
        tmp = np.copy(B[k+j])
        B[k+j] = B[k]
        B[k] = tmp

        for i in range(k+1,len(A)):
            m = A[i][k] / A[k][k]
            # A[i][k] = m
            for j in range(k,len(A)):
                A[i][j] = A[i][j] - A[k][j] * m
            B[i] = B[i] - B[k] * m
    # print("增广阵为")
    # print(A)
    # print(B)
    # 回代部分
    for i in range(len(A)-1,-1,-1):
        if i == len(A)-1 : 
            X[i] = B[i] / A[i][i]
            continue
        temp = 0
        for m in range(i+1,len(A)):
            temp += A[i][m] * X[m]
        X[i] = (B[i] - temp)/A[i][i]
    
    return X

        # for i in range(len(A[0])):
    # print(A)
            

if __name__ == "__main__":
    # print(A.size)
    # print(B)
    # test = np.array([
    #     [0.001,2.000,3.000],
    #     [-1,3.712,4.623],
    #     [-2,1.072,5.643]
    # ])
    # test_b = np.array([1.0,2.0,3.0]).reshape((-1,1))
    # ans = np.linalg.solve(test,test_b)
    # ans = ans.T
    # print("Answer is :")
    # print(ans)

    # outcome = column_main_solution(test,test_b)
    # outcome = outcome.T
    # print("Column domain solution's outcome is: ")
    # print(outcome)
    ans = np.linalg.solve(A,B)
    ans = ans.T
    print("标准答案为:")
    print(ans)

    outcome = column_main_solution(A,B)
    outcome = outcome.T
    print("列主元素法结果为: ")
    print(outcome)
    print("增广阵为：")
    print(np.append(A,B,axis=1))
    
    print("---------随机矩阵检测----------")
    ran_mar = np.random.rand(50,50)*100 
    ran_b = np.random.rand(50,1)*100
    # print(ran_mar)
    # print(ran_b)
    ans2 = np.linalg.solve(ran_mar,ran_b).T
    print("标准答案为:")
    print(ans2)

    outcome2 = column_main_solution(ran_mar,ran_b).T
    print("列主元素法结果为: ")
    print(outcome2)
    print("增广阵为：")
    print(np.append(ran_mar,ran_b,axis=1))