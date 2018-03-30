
def mark10(x,matrixname):
    month=[90,91,92,92]
    p=month[x]
    pm10season=np.zeros((25,p))
    for i in range(25):
        for j in range(p):
            pm10season[i][j]=pm10dailyColor[i][j+sum(month[0:x])]
    pm10seasonmark=np.zeros((3,3))
    
    for j in range(p-1):
      for i in range(25):
        if pm10season[i][j] == 1:
            n = 1 
        elif pm10season[i][j] == 2:
            n = 2
        elif pm10season[i][j] == 3:
            n = 3
        else:
            n = 0
            
        if pm10season[i][j+1] == 1:
            m = 1 
        elif pm10season[i][j+1] == 2:
            m = 2
        elif pm10season[i][j+1] == 3:
            m = 3
        else:
            m = 0            
        
        if(n != 0 and m != 0):
            pm10seasonmark[n-1][m-1] = pm10seasonmark[n-1][m-1]+1

    for i in range(3):
        if sum(pm10seasonmark[i])==0:
            matrixname[i]=0
        else:
            matrixname[i]=pm10seasonmark[i]/sum(pm10seasonmark[i])
    return matrixname
