import matplotlib.pyplot as plt
#Values for X axes
xvalues=[18,19,20,21,22,]
#Values por Y axes
yvaluesmex=[2190,1928,4837,1828,4329]
yvaluesuru=[1212,3787,1211,2111,6111]
#Style por visualization
plt.style.use("bmh")
#Name of X axes
plt.xlabel("Age")
#Name of Y axes
plt.ylabel("Salary")
#Type of visualization
plt.plot(xvalues,yvaluesmex,label="Mexico",color="k",linestyle="--",linewidth="3")
plt.plot(xvalues,yvaluesuru,label="Uruguay",color="#12f3",linestyle="-",linewidth="5")
#Title for visualization
plt.title("Salaries in the world")
#Show labels
plt.legend()
#Show visualization
plt.show()
