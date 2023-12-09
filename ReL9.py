import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = x**2 - 4
    return y

def dxf(x):
    y = 2*x
    return y

x0 = np.linspace(-10, 10, 1000)
theta = np.random.rand() * 8 - 4
print(f"Posicion inicial: {theta}")
lr = 0.01
x = []
y = []

for _ in range(2500):
    theta = theta - (lr * dxf(theta))
    if _ % 250 == 0:
        print(f"Pendiente de la posicion {round(theta, 2)}: {round(dxf(theta))}")
        x.append(theta)
        y.append(f(theta))
        plt.scatter(x, y, color="green")
        plt.plot(x, y, color="red")
        
theta = round(theta, 2)
print(f"Minimo local: {theta}")
plt.title("Gradient descent")
plt.plot(x0, f(x0), color="blue")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.ylim(-5, 10)
plt.xlim(-10, 10)
plt.axhline(0, color="black", alpha=0.5)
plt.axvline(0, color="black", alpha=0.5)
