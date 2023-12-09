import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return -3 + x1**2 + x2**2

def gradient_x1(x1, x2):
    return 0.4 * (x1 + x2) - 0.3 * x2

def gradient_x2(x1, x2):
    return 0.4 * (x1 + x2) - 0.3 * x1

lr = 1.5

x1_list = []
x2_list = []
y_list = []

# x1, x2 = np.random.rand(2) * 10 
x1 = -5.0
x2 = 5

for i in range(50):
    x1_list.append(x1)
    x2_list.append(x2)
    y_list.append(f(x1, x2))
    x1 = x1 - lr * gradient_x1(x1, x2)
    x2 = x2 - lr * gradient_x2(x1, x2)
    
X1 = np.arange(-5, 5, 0.01)
X2 = np.arange(-5, 5, 0.01)
X1, X2 = np.meshgrid(X1, X2)
Y = f(X1, X2)
fig = plt.figure()
ax = plt.subplot(111, projection="3d")
ax.plot_surface(X1, X2, Y, rstride=5, cstride=5, cmap= "gist_stern")
ax.plot(x1_list, x2_list, y_list, "bo--")