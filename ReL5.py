import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = 3 * (x ** 2) + 12 * x + 11
    return y

def dxf(x):
    y = 6*x + 12
    return y

x0 = np.linspace(-10, 10, 1000)
lr = 0.01
omega = np.random.rand() * 20 - 10
print(f"Posicion inicial: {omega}")
xL = []
yL = []

for _ in range(2500):
    omega = omega - (lr * dxf(omega))
    if _ % 25 == 0:
        xL.append(omega)
        yL.append(f(omega))
        plt.scatter(xL, yL, color = "green")
        plt.plot(xL, yL, color = "blue")

omega = round(omega, 2)
print(f"Punto minimo: {omega}")
print(f"Pendiente del punto minimo: {dxf(omega)}")
print(f"Altura en el eje de la y: {f(omega)}")
plt.plot(x0, f(x0), color="red")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color="black", alpha=0.5)
plt.axvline(0, color="black", alpha=0.5)
plt.grid(True)
plt.show()