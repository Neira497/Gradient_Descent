import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    z = 4*x**2 + y**2
    return z

def dxf(x):
    y = 8 * x
    return y

def dyf(y):
    x = 2*y
    return x

plt.ion()
x0 = np.linspace(-10, 10, 1000)
x1 = np.linspace(-10, 10, 1000)
fig = plt.figure()
ax = plt.subplot(111, projection="3d")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
lr = 0.1
x0, x1 = np.meshgrid(x0, x1)
z = f(x0, x1)
theta = [-10, 0]
print(theta)
ax.plot_surface(x0, x1, z, rstride=5, cstride=5, cmap="gist_stern")

xlist = []
ylist = []
zlist = []

for i in range(250):
    xlist.append(theta[0])
    ylist.append(theta[1])
    zlist.append(f(theta[0], theta[1]))
    theta[0] = theta[0] - (lr * dxf(theta[0]))
    theta[1] = theta[1] - (lr * dyf(theta[1]))
    print(theta)
    ax.plot(xlist, ylist, zlist, "bo--")
    
theta[0] = round(theta[0], 2)
theta[1] = round(theta[1], 2)
print(theta)