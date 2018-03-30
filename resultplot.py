import matplotlib.pyplot as plt
import numpy as np
# The slices will be ordered and plotted counter-clockwise.
labels = ['good', 'moderate', 'unhealthy for \n sensitive groups', 'unhealthy']
labels1 = ['good', 'moderate', 'unhealthy for \n sensitive groups']
colors = ['lime', 'yellow', 'orange', 'red']
colors1 = ['lime', 'yellow', 'orange']
  # explode a slice if required
seasons=['spring','summer','fall','winter']
position=[231,232,234,235]
plt.subplot(231)
plt.pie(result['year10'], explode=(0,0,0), colors=colors,autopct='%1.1f%%',pctdistance=1.2)        
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75, fc='white')
plt.text(0,0,'pm10',fontsize=15,horizontalalignment='center',
     verticalalignment='center')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.subplot(232)
plt.pie(result['year25'], explode=(0,0,0,0), colors=colors,autopct='%1.1f%%',pctdistance=1.2)
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75, fc='white')
plt.text(0,0,'pm25',fontsize=15,horizontalalignment='center',
     verticalalignment='center')

plt.legend(labels,bbox_to_anchor=(1.2,1),fontsize=7)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.show()
plt.savefig('pollutant.png',dpi=(200))

#test= np.delete(finalresult25[1],2)

for i in range(4):
    if i ==0 or i==1:
        plt.subplot(position[i])
        plt.pie(np.delete(result[25][i],3),explode=(0,0,0),colors=colors,autopct='%1.1f%%', pctdistance=1.2)
        centre_circle = plt.Circle((0,0),0.75, fc='white')
    else:
        plt.subplot(position[i])
        plt.pie(result[25][i],explode=(0,0,0,0),colors=colors,autopct='%1.1f%%', pctdistance=1.2)
        centre_circle = plt.Circle((0,0),0.75, fc='white')
    plt.text(0,0,seasons[i],fontsize=12,horizontalalignment='center',verticalalignment='center')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.grid(True)
plt.legend(labels,bbox_to_anchor=(2.2,2),fontsize=7)
plt.show()
plt.savefig('pm25season.png',dpi=(150))

for i in range(4):
    if i ==0 or i==1:
        plt.subplot(position[i])
        plt.pie(np.delete(result[10][i],2),explode=(0,0),colors=colors,autopct='%1.1f%%', pctdistance=1.2)
        centre_circle = plt.Circle((0,0),0.75, fc='white')
    else:
        plt.subplot(position[i])
        plt.pie(result[10][i],explode=(0,0,0),colors=colors,autopct='%1.1f%%', pctdistance=1.2)
        centre_circle = plt.Circle((0,0),0.75, fc='white')
    plt.text(0,0,seasons[i],fontsize=12,horizontalalignment='center',verticalalignment='center')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.grid(True)
plt.legend(labels1,bbox_to_anchor=(2.2,2),fontsize=7)
plt.show()
plt.savefig('pm10season.png',dpi=(150))



