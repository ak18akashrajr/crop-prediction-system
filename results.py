import matplotlib.pyplot as plt  
# data to display on plots  
x = ["Ridge Regression","Linear Regression","Decision Tree","Random Forest"]  
y = [0.4776941708642126,0.4776945553749764,"0.9942978591052822","0.9670230540465157"]  
  
# This will plot a simple bar chart 
plt.bar(x, y) 
  
# Title to the plot 
plt.title("Bar Chart") 
  
# Adding the legends 
plt.legend(["bar"]) 
plt.show()