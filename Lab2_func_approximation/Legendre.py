from scipy.integrate import quad, dblquad, tplquad, nquad

class Legendre :
    interval = []
    coeffi = []
    outcome = []
    def __init__(self,a):
        temp = a #得到逼近区间
        # 需要将x线性变化到[-1,1]区间中
        self.interval.append((temp[1]-temp[0])/2)
        self.interval.append((temp[0] + temp[1])/2)
        # print(self.interval)

    def calculation(self,k,c):
        for i in range(k+1):
            # print
            # 根据次数来计算多少个系数
            out = 0
            if i == 0: 
                # f = 1/(1+c*(self.interval[0]*t+self.interval[1])**2)
                out,err = quad(lambda t: (1/(1+c*(self.interval[0]*t+self.interval[1])**2)),-1,1)
                out = out/2
               
            if i == 1:
                # t = symbols('t')
                # f = (t)/(1+c*(self.interval[0]*t+self.interval[1])**2)
                out,err = quad(lambda t: (t/(1+c*(self.interval[0]*t+self.interval[1])**2)),-1,1)
                out = out *3.0/2
           
            if i == 2 :
                # t = symbols('t')
                # f = (3*(t**2)-1)/(2*(1+c*(self.interval[0]*t+self.interval[1])**2))
                out,err = quad(lambda t: ((3*(t**2)-1)/(2*(1+c*(self.interval[0]*t+self.interval[1])**2))),-1,1)
                out = out *5.0/2
               

            if i == 3 :
                # t = symbols('t')
                # f = (5*(t**3)-3*(self.interval[0]*t+self.interval[1]))/(2*(1+c*(self.interval[0]*t+self.interval[1])**2))
                out,err = quad(lambda t: ((5*(t**3)-3*(t))/(2*(1+c*(self.interval[0]*t+self.interval[1])**2))),-1,1)
                out = out * 7.0/2

            self.coeffi.append(out)
        
    def cal_test(self,test_set):
        # print(self.coeffi)
        for i in range(len(test_set)):
            temp = test_set[i]
            out = 0
            for j in range(len(self.coeffi)):
                temp1 = self.functio1(j,temp)
                out = out + self.coeffi[j]*temp1
            self.outcome.append(out)
        return self.outcome

    def functio1(self,j,x):
        if j == 0:
            return 1
        elif j == 1:
            return x
        elif j == 2:
            return 3/2*x**2-1/2
        elif j == 3:
            return 5/2*x**3-3/2*x
            
