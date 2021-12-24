 ans = np.linalg.solve(A,B)
    ans = ans.T
    print("Answer is :")
    print(ans)

    outcome = column_main_solution(A,B)
    outcome = outcome.T
    print("Column domain solution's outcome is: ")
    print(outcome)
    
    print("---------随机矩阵检测----------")
    ran_mar = np.random.rand(50,50)*100 
    ran_b = np.random.rand(50,1)*100
    # print(ran_mar)
    # print(ran_b)
    ans2 = np.linalg.solve(ran_mar,ran_b).T
    print("Answer is :")
    print(ans2)

    outcome2 = column_main_solution(ran_mar,ran_b).T
    print("Column domain solution's outcome is: ")
    print(outcome2)