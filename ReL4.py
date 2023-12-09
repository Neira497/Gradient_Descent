import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = 3 * (x ** 2) - 5 * x + 2
    return y

def fdx(x):
    y = 6 * x - 5
    return y

x0 = np.linspace(-1, 1, 100)
lr = 0.01

xL = []
yL = []
delta = np.random.rand() * 2 - 1
print(f"Posicion inicial: {delta}")

for _ in range(2500):
    delta = delta - (lr * fdx(delta))
    if _ % 10 == 0:
        xL.append(delta)
        yL.append(f(delta))
        plt.scatter(xL, yL, color = "green")
        plt.plot(xL, yL, color = "red")

delta = round(delta, 2)        
print(f"valor del minimo local: {delta}")
print(f"Derivada del minimo local: {fdx(delta)}")
plt.title("Desenso del gradiente")
plt.plot(x0, f(x0), color = "blue")
plt.ylabel("Valor de y")
plt.xlabel("Valor de x")
plt.show()