# # list = [19, 25, 31, 38, 44]
# # out = 0
# # for i in range(len(list)):
# #     out+=list[i]**4
# # print(out)

# # list_y = [19, 32.3, 49.0, 73.3, 97.8]
# # out1 = 0
# # for i in range(len(list_y)):
# #     out1+=list_y[i]*(list[i]**2)
# # print(out1)


# # import numpy as np
# # coefficent = [[5, 5327],[5327, 7277699]]
# # y = [271.4, 369321.5]
# # outcome = np.linalg.solve(coefficent,y)
# # print(outcome)

# import math
# import numpy as np
# list = [ 5, 10 ,15, 20, 25, 30, 35, 40, 45, 50, 55]
# y = [1.27, 2.16, 2.86, 3.44, 3.87, 4.15, 4.37, 4.51, 4.58, 4.62, 4.64]
# sum = 0
# for i in range(len(list)):
#     sum += 1/(list[i]*list[i])
# print(sum)

# sumy = 0
# for i in range(len(y)):
#     sumy +=math.log(y[i]) * (1/list[i])
#     # *list[i]
# print(sumy)

# coeffi = np.array([[11,0.60398],[0.60398,0.06232]])
# y =  np.array([13.63964929174793,0.5303305153520731])
# outcome = np.linalg.solve(coeffi,y)
# print(outcome)

# from numpy import testing


X = [1,2,3]
Y = X
X = [4,5,6]
Y[0:3] = X[0:3]

print(Y)