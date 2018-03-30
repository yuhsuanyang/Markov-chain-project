def mark25(x,matrixname):
    month=[90,91,92,92]
    p=month[x]
    pm25season=np.zeros((25,p))
    for i in range(25):
        for j in range(p):
            pm25season[i][j]=pm25dailyColor[i][j+sum(month[0:x])]
    pm25seasonmark=np.zeros((4,4))
    
    for j in range(p-1):
      for i in range(25):
        if pm25season[i][j] == 1:
            n = 1 
        elif pm25season[i][j] == 2:
            n = 2
        elif pm25season[i][j] == 3:
            n = 3
        elif pm25season[i][j] == 4:
            n = 4 
        else:
            n = 0
            
        if pm25season[i][j+1] == 1:
            m = 1 
        elif pm25season[i][j+1] == 2:
            m = 2
        elif pm25season[i][j+1] == 3:
            m = 3
        elif pm25season[i][j+1] == 4:
            m = 4
        else:
            m = 0            
        
        if(n != 0 and m != 0):
            pm25seasonmark[n-1][m-1] = pm25seasonmark[n-1][m-1]+1

    for i in range(4):
        if sum(pm25seasonmark[i])==0:
            matrixname[i]=0
        else:
            matrixname[i]=pm25seasonmark[i]/sum(pm25seasonmark[i])
    return matrixname