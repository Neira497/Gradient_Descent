import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = (x + 2)**2
    return y

def fdx(x):
    derivada = 2 * (x + 2)
    return derivada

x = np.linspace(-5, 5, 10000)

delta = np.random.rand() * 10 - 5
print(f"Posicion inicial: {delta}")
lr = 0.01

x_list = []
y_list = []

for i in range(2500):
    delta = delta - lr * fdx(delta)
    if i % 50 == 0:
        x_list.append(delta)
        y_list.append(f(delta))
        plt.scatter(x_list, y_list, c="green")
        plt.plot(x_list, y_list, c="red")

plt.plot(x, f(x), c="blue", alpha=0.3)
plt.show()

delta = round(delta, 1)
print(f"Minimo local: {delta}")
print(f"Derivada del minimo local: {fdx(delta)}")
