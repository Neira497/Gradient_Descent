import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = 2*(x**2) + 9*x + 10
    return y

def dxf(x):
    y = 4*x+9
    return y

x0 = np.linspace(-10, 10, 1000)
theta = 10
xlist = [theta]
ylist = [f(theta)]
lr = 0.1

print(f"Posicion inicial {theta}")

for _ in range(4000):
    theta = theta - (lr * dxf(theta))
    if _ % 200 == 0:
        plt.plot(xlist, ylist, color = "red")
        plt.scatter(xlist, ylist, marker = "o", color = "green", alpha = 0.2)
        xlist.append(theta)
        ylist.append(f(theta))

theta = round(theta, 5)
print(f"Minimo local: {theta}")
print(f"Derivada del minimo local: {dxf(theta)}")
plt.plot(x0, f(x0), color = "blue")
plt.title("Desenso del gradiente")
plt.xlabel("Valor de x")
plt.ylabel("Valor de y")
plt.show()
