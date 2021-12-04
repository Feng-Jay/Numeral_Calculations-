import numpy as np

class Square :
    x = []
    y = []
    coeffi_martix = []
    outcome_vector = []
    coeffi_o = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def calculation(self,k):
        for i in range(k+1):
            row = []
            for j in range(k+1):
                temp = 0
                for n in range(len(self.x)):
                    temp += pow(self.x[n], i+j)
                row.append(temp)
            # 系数矩阵构造完成
            temp_y = 0
            for m in range(len(self.x)):
                temp_y += pow(self.x[m],i) * self.y[m]

            self.coeffi_martix.append(row)
            self.outcome_vector.append(temp_y)
        self.coeffi_o = np.linalg.solve(self.coeffi_martix,self.outcome_vector)
        # print(self.coeffi_martix)
        # print(self.outcome_vector)
        # print(self.coeffi_o)

    def outcome(self,test_set):
        outcome = []
        for i in range(len(test_set)):
            temp = 0
            for j in range(len(self.coeffi_o)):
                temp += self.coeffi_o[j]*pow(test_set[i],j)
                # print("j=",j)
            outcome.append(temp)
        return outcome

