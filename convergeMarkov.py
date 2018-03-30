def convergeMarkov(MarkovMat,iter_n):
    iterHistory={}
    iterHistory[1]=np.dot(MarkovMat,MarkovMat)
    for i in range(2,iter_n):
        iterHistory[i] = np.dot(MarkovMat,iterHistory[i-1])
        for y in range(3):
            for z in range(3):
                iterHistory[i][y][z] = np.round(iterHistory[i][y][z],4)       
    test_n = 1
    
    while not((iterHistory[test_n][0][0]==iterHistory[test_n+1][0][0]) and (iterHistory[test_n][0][1]==iterHistory[test_n+1][0][1])and(iterHistory[test_n][0][2]==iterHistory[test_n+1][0][2])and(iterHistory[test_n][1][0]==iterHistory[test_n+1][1][0])and(iterHistory[test_n][1][1]==iterHistory[test_n+1][1][1])and(iterHistory[test_n][1][2]==iterHistory[test_n+1][1][2])and(iterHistory[test_n][2][0]==iterHistory[test_n+1][2][0])and(iterHistory[test_n][2][1]==iterHistory[test_n+1][2][1])and(iterHistory[test_n][2][2]==iterHistory[test_n+1][2][2])):
    #while not((iterHistory[test_n]==iterHistory[test_n+1])):  
        test_n = test_n+1
    print('   The matrix converge at the',test_n,'th time!!!')
    return iterHistory,test_n