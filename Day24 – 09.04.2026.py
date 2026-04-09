import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(10)
y = np.random.randn(10)
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.1,0.1])
axes1.set_xlabel('AA')
axes1.plot(x,y)
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.plot(y,x)
plt.xlabel('A')
plt.show()

fig,axes =plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y)
axes[0].set_xlabel('A')
axes[1].plot(y,x)
plt.show()

#figure sizw DPI
fig = plt.figure(figsize=(3,2),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel()
ax.set_title()
plt.show()

fig,axes =plt.subplots(2,1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
plt.show()

fig.savefig('picture.png',dpi=200)

fig = plt.figure(figsize=(3,2),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x+1,label='L1')
ax.plot(x,x+2,label='L2')
ax.legend(loc=0)
ax.legend(loc=(0.1,0.1))
plt.show()