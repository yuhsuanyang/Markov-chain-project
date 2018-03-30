''' 
    2017 Autumn Semester - Operation Research - Final Report 
    Topic: 
        
        Using Markov Probability Matrix to Evaluate Air Quality in Northern Taiwan
    
    Member: 
        曾令佳 能源國際學士學位學程學士班 F04026052
        楊于萱 能源國際學士學位學程學士班 F04036196
        林尚緯 能源國際學士學位學程學士班 F04036015



'''

'''======= Operation Manuel 操作手冊 ======= 
 
    Step1. run function file 'converMarkov.m'
           run function file 'p m10markfunction.m'
           run function file 'pm25markfunction.m'
    
    Step2. run this file 'ORFinalMarkovMAIN.m'
    
    Step3. Wait for the results! :)  
    
    Step4. run the 'resultplot.py' file,
           we will export two graphs to your current folder
           for you to see the Transition Matrix results comparison! :)  


'''


#======= Import Libraries =======
import pandas as pd
import numpy as np
from datetime import datetime
from collections import Counter
import math
import matplotlib.pyplot as plt
#================================


#=====================================================
# ============ part.1 Data Prearrangement ============
#=====================================================
pm = pd.ExcelFile('pm.xlsx')
pm.sheet_names
sheetX = pm.parse('工作表1') 
print('\n\n\n Loading data... please wait.......')
banqiao=sheetX.loc[sheetX['station']=='Banqiao']
pm25=pd.Series(sheetX['PM2.5(μg/m3)'] )
pm10=pd.Series(sheetX['PM10(μg/m3)'] )
b=pd.Series(sheetX['PM10(μg/m3)'])
time=pd.DataFrame(sheetX['time']) 

print('\n\n\n We are now rearranging the Air Quality Data, please wait! :)\n...\n...\n...')

for i in range(218640):
    if type(pm10[i]) == str or math.isnan(pm10[i])==True:
        pm10[i]=0
for i in range(218640):
    if type(pm25[i]) == str or math.isnan(pm25[i])==True :
        pm25[i]=0
a= pm10.tolist()
b= pm25.tolist()
station = pd.Series(sheetX['station'])
print('\n We will soon begin to count some numbers.')
print('   If you see a few numbers being print out, don''t worry! Everythings are in control!\n..\n..') 

#print (time['time'].dt.date)
s1=np.zeros((1,25))
for i in range(25):
    if i == 1 or i == 8 or i == 20 or i == 24:
        s1[0][i]=8736
    elif i == 13:
        s1[0][i]=8664
    elif i == 7:
        s1[0][i]=8688
    elif i==10 or i ==21:
        s1[0][i]=8712
    else:
        s1[0][i]=8760
        
s2=['Banqiao','Cailiao','Datong','Dayuan','Guanyin','Guting','Keelung','Linkou','Longtan','Pingzhen','Sanchong','Shilin','Songshan','Tamsui','Taoyuan','Tucheng','Wanhua','Wanli','Xindian','Xinzhuang','Xizhi','Yangming','Yonghe','Zhongli','Zhongshan']

dataMat=banqiao['time']
d=np.zeros((8760,25))

count = 0
for j in range(25):
    #print(j)
    for i in range(8760):
        if dataMat[i] == time['time'][count]:
            d[i][j] = a[count] 
            count=count+1
    count = int(sum(s1[0][0:j-1]))
    
e=np.zeros((8760,25))
count = 0
for j in range(25):
    print(j)
    for i in range(8760):
        if dataMat[i] == time['time'][count]:
            e[i][j] = b[count] 
            count=count+1
    count = int(sum(s1[0][0:j-1]))
    
#=====================================================    
# ============ part.2 Color Labelling ================
#=====================================================    
D1= np.transpose(d)
D2=np.reshape(D1,(9125,24))
D=np.zeros((1,9125))
        
for i in range(9125) :
    if 24-list(D2[i]).count(0) != 0 :
        D[0][i]=sum(D2[i])/(24-list(D2[i]).count(0))
    else :
        D[0][i]=0
pm10daily=np.reshape(D,(25,365))

E1= np.transpose(e)
E2=np.reshape(E1,(9125,24))
E=np.zeros((1,9125))
print('\n\n\n Color labelling the Air Quality Data....... :)\n..\n..')        
for i in range(9125) :
    if 24-list(E2[i]).count(0) != 0 :
        E[0][i]=sum(E2[i])/(24-list(E2[i]).count(0))
    else :
        E[0][i]=0
pm25daily=np.reshape(E,(25,365))

pm25dailyColor = np.zeros((25,365))
for j in range(365):
    for i in range(25): # For PM2.5
        A=pm25daily[i][j]
        if(A > 0 and A <= 15.4):
            A = 1
        elif( A > 15.4 and A <= 35.4 ):
            A = 2
        elif( A > 35.4 and A <= 54.4 ):
            A = 3
        elif( A > 54.4 and A <= 150.4 ):
            A = 4
        elif( A > 150.4 and A <= 250.4 ):
            A = 5
        elif( A > 250.4 and A <= 350.4 ):
            A = 6
        elif ( A > 350.4 and A <= 500.4):
            A = 7
        elif A == 0 :
            A=0
        else:
            print("Wrong Range in the A ")
        pm25dailyColor[i][j]=A
pm10dailyColor = np.zeros((25,365))
for j in range(365):
   for i in range(25): # For PM10
       B = pm10daily[i][j]
       if(B > 0 and B <= 54 ):
           B = 1
       elif(B > 54 and B <= 125 ):
           B = 2
       elif(B > 125 and B <= 254 ):
           B = 3
       elif  ( B > 254 and B <= 354 ):
           B = 4
       elif( B > 354 and B <= 424 ):
           B = 5
       elif  ( B > 424 and B <= 504 ):
           B = 6
       elif  ( B > 504 and B <= 604 ):
           B = 7
       elif B==0 :
           B=0
       else:
           print("Wrong Range in the b")
       pm10dailyColor[i][j] = B
       
#=====================================================   
#========== part.3 Markov Probability Matrix =========
#=====================================================
print('\n\n\n Calculating the Markov Probability Matrix.....')  
# === PM2.5 Markov Annual Probability ===
print('\n\n Please Wait.......\n..\n..')         
pm25Mark = np.zeros((4,4))
for j in range(364):
    for i in range(25):
        if pm25dailyColor[i][j] == 1:
            n = 1 
        elif pm25dailyColor[i][j] == 2:
            n = 2
        elif pm25dailyColor[i][j] == 3:
            n = 3
        elif pm25dailyColor[i][j] == 4:
            n = 4 
        else:
            n = 0
            
        if pm25dailyColor[i][j+1] == 1:
            m = 1 
        elif pm25dailyColor[i][j+1] == 2:
            m = 2
        elif pm25dailyColor[i][j+1] == 3:
            m = 3
        elif pm25dailyColor[i][j+1] == 4:
            m = 4 
        else:
            m = 0            
        
        if(n != 0 and m != 0):
            pm25Mark[n-1][m-1] = pm25Mark[n-1][m-1]+1
pm25Markpro = np.zeros((4,4))
for i in range(4):
    pm25Markpro[i]=pm25Mark[i]/sum(pm25Mark[i])

# PM10 Markov Annual Probability            
pm10Mark = np.zeros((3,3))
for j in range(364):
    for i in range(25):
        if pm10dailyColor[i][j] == 1:
            n = 1 
        elif pm10dailyColor[i][j] == 2:
            n = 2
        elif pm10dailyColor[i][j] == 3:
            n = 3
        else:
            n = 0
            
        if pm10dailyColor[i][j+1] == 1:
            m = 1 
        elif pm10dailyColor[i][j+1] == 2:
            m = 2
        elif pm10dailyColor[i][j+1] == 3:
            m = 3
        else:
            m = 0            
        
        if(n != 0 and m != 0):
            pm10Mark[n-1][m-1] = pm10Mark[n-1][m-1]+1
pm10Markpro = np.zeros((3,3))
for i in range(3):
    pm10Markpro[i]=pm10Mark[i]/sum(pm10Mark[i])
    
M25_history = {}
M25_history[1]=np.dot(pm25Markpro,pm25Markpro)
for i in range(2,50):
    M25_history[i] = np.dot(pm25Markpro,M25_history[i-1])
    for y in range(4):
        for z in range(4):
            M25_history[i][y][z] = np.round(M25_history[i][y][z],4)

M10_history = {}
M10_history[1]=np.dot(pm10Markpro,pm10Markpro)
for i in range(2,50):
    M10_history[i] = np.dot(pm10Markpro,M10_history[i-1])
    for y in range(3):
        for z in range(3):
            M10_history[i][y][z] = np.round(M10_history[i][y][z],4)

print('\n\n\n======= ANNUAL AIR QUALITY REPORT =======\n')            
print('\n PM2.5 Annual Data Markov Probability')
M25_history, M25_history_count = convergeMarkov(pm25Markpro,20)
print('\n PM10 Annual Data Markov Probability')
M10_history,M10_history_count = convergeMarkov(pm10Markpro,20)  
iter_n=30  
print('\n\n\n======= SEASONAL AIR QUALITY REPORT =======\n')  
pm25winterpro=np.zeros((4,4))
pm25springpro=np.zeros((4,4))
pm25summerpro=np.zeros((4,4))
pm25fallpro=np.zeros((4,4))
mark25(0,pm25winterpro)
mark25(1,pm25springpro)
mark25(2,pm25summerpro)
mark25(3,pm25fallpro)
print('\n === PM2.5 Markov Probability Matrix ===')
print(' 。Spring:',end='')
Hist_pm25_spring,count_pm25_spring = convergeMarkov(pm25springpro,iter_n)
print('\n 。Summer:',end='')
Hist_pm25_summer,count_pm25_summer = convergeMarkov(pm25summerpro,iter_n)
print('\n 。Fall:',end='')
Hist_pm25_fall,count_pm25_fall = convergeMarkov(pm25fallpro,iter_n)
print('\n 。Winter:',end='')
Hist_pm25_winter,count_pm25_winter = convergeMarkov(pm25winterpro,iter_n)   


pm10winterpro=np.zeros((3,3))
pm10springpro=np.zeros((3,3))
pm10summerpro=np.zeros((3,3))
pm10fallpro=np.zeros((3,3))
mark10(0,pm10winterpro)
mark10(1,pm10springpro)
mark10(2,pm10summerpro)
mark10(3,pm10fallpro)

print('\n ===== PM10 Markov Probability Matrix =====')
print(' 。Spring:',end='')
Hist_pm10_spring,count_pm10_spring = convergeMarkov(pm10springpro,iter_n)
print('\n 。Summer:',end='')
Hist_pm10_summer,count_pm10_summer = convergeMarkov(pm10summerpro,iter_n)
print('\n 。Fall:',end='')
Hist_pm10_fall,count_pm10_fall = convergeMarkov(pm10fallpro,iter_n)
print('\n 。Winter:',end='')
Hist_pm10_winter,count_pm10_winter = convergeMarkov(pm10winterpro,iter_n)       


print('\n\n\n======= SEASONAL AIR QUALITY GRAPHs =======\n')  
#PM2.5 
plt.subplot(111)
plt.plot(Hist_pm25_spring[count_pm25_spring][0],'-o',color='g', label = 'Spring',linewidth=2)
plt.plot(Hist_pm25_summer[count_pm25_summer][0],'-^',color='r', label = 'Summer',linewidth=2)
plt.plot(Hist_pm25_fall[count_pm25_fall][0],'-s',color='orange', label = 'Fall',linewidth=2)
plt.plot(Hist_pm25_winter[count_pm25_winter][0],'-+',color='steelblue', label = 'Winter',linewidth=2)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('PM2.5 Seasonal 4 Conditions Markov')
plt.xlabel('Condition(0,1,2,3)')
plt.ylabel('Probability')
plt.grid(True,alpha = 0.2)
plt.show()

plt.subplot(111)
plt.plot(Hist_pm10_spring[count_pm10_spring][0],'-o',color='g', label = 'Spring',linewidth=2)
plt.plot(Hist_pm10_summer[count_pm10_summer][0],'-^',color='r', label = 'Summer',linewidth=2)
plt.plot(Hist_pm10_fall[count_pm10_fall][0],'-s',color='orange', label = 'Fall',linewidth=2)
plt.plot(Hist_pm10_winter[count_pm10_winter][0],'-+',color='steelblue', label = 'Winter',linewidth=2)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('PM10 Seasonal 4 Conditions Probability')
plt.xlabel('Condition(0,1,2,3)')
plt.ylabel('Probability')
plt.grid(True,alpha = 0.2)
plt.show()


result={10:{0:Hist_pm10_spring[count_pm10_spring][1],1:Hist_pm10_summer[count_pm10_summer][1],2:Hist_pm10_fall[count_pm10_fall][1],3:Hist_pm10_winter[count_pm10_winter][1]},\
            25:{0:Hist_pm25_spring[count_pm25_spring][2],1:Hist_pm25_summer[count_pm25_summer][2],2:Hist_pm25_fall[count_pm25_fall][2],3:Hist_pm25_winter[count_pm25_winter][2]},\
            'year10':M10_history[19][2],'year25':M25_history[19][2]}




