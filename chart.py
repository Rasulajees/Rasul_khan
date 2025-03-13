import matplotlib.pyplot as plt
import numpy as np

#Line chart:
x=[10,20,30,45,67]
y=[1,2,3,4,5]

plt.plot(x,y)
plt.title("simple plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
#----------------------------------------------------------------
#Pie chart:
y=np.array([10,20,30,45,67])
my_labels=["Apples","Bananas","Cherries","Dates","Dragon fruit"]
plt.pie(y,labels=my_labels)
plt.title("simple pie chart")
plt.show()
#----------------------------------------------------------------
#Bar chart:

x=[10,20,30,45,67]
y=[1,2,3,4,5]

plt.bar(x,y)
plt.title("simple bar chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
#----------------------------------------------------------------
#Scatter plot:
x=[10,20,30,45,67]
y=[1,2,3,4,5]

plt.scatter(x,y)
plt.title("simple scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#----------------------------------------------------------------
#Histogram:
x=[10,20,30,45,67]

plt.hist(x)
plt.title("simple histogram")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
