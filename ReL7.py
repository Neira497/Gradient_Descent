import matplotlib.pyplot as plt
import numpy as np

funcion = (lambda x: x**2 - 2*x + 3,  # Formula a optimizar
           lambda x: 2*x - 2)         # Derivada de la formula

x0 = np.linspace(-5, 5, 1000)
lr = 0.01
delta = np.random.rand() * 10 - 5
print(f"Posicion inicial: {delta}")
x = []
y = []

for _ in range(2500):
    delta = delta - (lr * funcion[1](delta))
    if _ % 500 == 0:
        x.append(delta)
        y.append(funcion[0](delta))
        plt.scatter(x, y, marker="o", color = "green")
        plt.plot(x, y, color="red")

delta = round(delta, 2)
print(f"Minimo local: {delta}")
print(f"Valor de la pendiente en el minimo local: {funcion[1](delta)}")
plt.plot(x0, funcion[0](x0), color="blue")
plt.grid(True)
plt.xlim(-5, 5)
plt.axhline(0, color="black", alpha=0.5)
plt.axvline(0, color="black", alpha=0.5)
plt.show()