import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = 2 * (x**2) - 4 * x - 1
    return y

def dx(x):
    y = 4*x - 4
    return y

x0 = np.linspace(-4, 4, 100)
delta = np.random.rand() * 8 - 4
print(f"Posicion inicial: {delta}")
xl = []
yl = []
lr = 0.01

for _ in range(2500):
    delta = delta - (lr * dx(delta))
    if _ % 25 == 0:
        xl.append(delta)
        yl.append(f(delta))
        plt.scatter(xl, yl, color = "green", marker = "o")
        plt.plot(xl, yl, color = "red")
        
delta = round(delta, 2)
print(f"Minimo local: {delta}")
print(f"Valor de la pendiente: {dx(delta)}")
plt.plot(x0, f(x0), color = "blue")
plt.title("Desenso del gradiente")
plt.grid(True)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.axhline(0, color="black", alpha=0.5)
plt.axvline(0, color = "black", alpha=0.5)
plt.show()