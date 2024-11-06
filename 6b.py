import matplotlib.pyplot as plt
overs=[0,1,2,3,4,5,6,7,10,11,12,1,3,14,15,16,17,18,19]
runs=[7,10,16,22,18,19,16,12,18,15,16,18,12,14,13,10,16,14,13,]
plt.plot(overs,runs,marker='x',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("over",color='red')
plt.ylabel("runs",color='blue')
plt.title("Varsha HA-1KI23CS175-linearplot")
plt.show()