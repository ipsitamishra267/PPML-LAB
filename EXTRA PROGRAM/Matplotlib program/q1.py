import matplotlib
print(matplotlib.__version__)
import matplotlib.pyplot as plt
x = [1, 2, 3, 4] 
y = [10, 20, 25, 30] 
plt.plot(x, y) 
plt.show()
plt.plot(x, y, linestyle='--')
plt.show()
plt.plot(x,y,color='red')
plt.show()
plt.plot(x,y,marker='o') 
plt.show()