import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**3 + 2*x**2 + 1
    return y

def dxf(x):
    y = 3*(x**2) + 4*x
    return y
x0 = np.linspace(-10, 10, 1000)
alpha = 1.55
print(f"Posicion inicial: {alpha}")
lr = 0.1
x = [alpha]
y = [f(alpha)]

for i in range(2500):
    alpha = alpha - (lr * dxf(alpha))
    if i % 500 == 0:
        print(f"Pendiente de la posicion {round(alpha, 2)}: {round(dxf(alpha),1)}")
        plt.scatter(x, y, color = "green", marker="o")
        plt.plot(x, y, color = "red")
        x.append(alpha)
        y.append(f(alpha))

alpha = round(alpha, 2)
print(f"Minimo local: {alpha}")
plt.title("Desenso del gradiente")
plt.xlabel("Eje X")
plt.ylabel("Eje y")
plt.plot(x0, f(x0), color="blue")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color="black", alpha=0.5)
plt.axvline(0, color="black", alpha=0.5)
plt.grid(True)
plt.plot()
