import math

class T:
    standard = 0
    h = 0
    a = []
    x = []
    y = []
    counter = 0
    outcome = 0
    precision = 0

    def __init__(self,standard,h,a,x,y,precision):
        self.standard = standard
        self.h = h
        self.a =a 
        self.x = x
        self.y = y
        self.counter = 0
        self.outcome = 0
        self.precision = precision

    def fx(self,x):
        temp = math.sqrt(x) * math.log(x)
        return temp
    
    def calculation(self):
        # print(len(self.x))
        for i in range(0,len(self.x)-1):
            self.outcome += self.fx(self.x[i])+ self.fx(self.x[i+1])
        self.outcome = (self.h/2) * self.outcome
        # print("T结果: ",self.outcome)
        diff = abs(self.standard - self.outcome)
        # print("误差为: ", diff)
        while diff > self.precision :
            self.outcome = 0
            temp = 0
            self.h = self.h /2
            self.counter +=1
            i = 0
            self.x = []
            while temp + self.h <= self.a[1] :
                temp = self.a[0] + i*self.h
                i += 1
                self.x.append(temp)
            # print(self.x)
            # input()
            for i in range(0,len(self.x)-1):
                self.outcome += self.fx(self.x[i])+ self.fx(self.x[i+1])
            self.outcome = (self.h/2) * self.outcome
            diff = abs(self.standard - self.outcome)

            # print("diff= ", diff)
        
        print("T结果: ",self.outcome)
        diff = abs(self.standard - self.outcome)
        print("误差为: ", diff)
        print("划分次数为: ", self.counter)
        print("步长h为: ", self.h)



