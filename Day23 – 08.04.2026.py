import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
#functional
plt.plot(x,y)
plt.xlabel('apple')
plt.ylabel('orange')
plt.title('fruit realtionship')
plt.show()

plt.subplot(1,2,1) #图片位置
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()

#oo
fig=plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #[left, bottom, width, height]
axes.plot(x,y)
axes.set_xlabel('O')
axes.set_ylabel('a')
axes.set_title('r')
plt.show()

fig=plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.4,0.6,0.2])
axes1.plot(x,y)
axes2.plot(y,x)
axes2.set_title()
plt.show()

