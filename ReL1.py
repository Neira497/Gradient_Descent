import matplotlib.pyplot as plt
import numpy as np
# Definir la funcion original
def f(x1, x2):
    return np.sin(1 / 2 * x1 ** 2 - 1 / 4 * x2 ** 2 + 3) * np.cos(2 * x1 + 1 - np.e ** x2)

# Funcion de gradiente (funcion derivada)
def gradient_x1(x1, x2):
        return 0.4 * (x1 + x2) - 0.3 * x2

def gradient_x2(x1, x2):
    return 0.4 * (x1 + x2) - 0.3 * x1

# Definir la tasa de aprendizaje
eta = 0.05

# Definir la lista de pistas de x1, x2, e y
x1_list = []
x2_list = []
y_list = []

#Definir la posicion inicial
# x1, x2 = np.random.rand(2) * 4 - 2
x1, x2 = -1.7, -0.3

for i in range(50):
    x1_list.append(x1)
    x2_list.append(x2)
    y_list.append(f(x1, x2))
    x1 = x1 - eta * gradient_x1(x1, x2)
    x2 = x2 - eta * gradient_x2(x1, x2)

# display(x1_list)
# display(x2_list)
# display(y_list)

X1 = np.arange(-2, 2, 0.01)
X2 = np.arange(-2, 2, 0.01)

X1, X2 = np.meshgrid(X1, X2)
Y = f(X1, X2)
fig = plt.figure()
ax = plt.subplot(111, projection="3d")
ax.plot_surface(X1, X2, Y, rstride=5, cstride=5, cmap= "rainbow")
ax.plot(x1_list, x2_list, y_list, "bo--")