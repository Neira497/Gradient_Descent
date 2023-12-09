import numpy as np
import matplotlib.pyplot as plt

def f(x, y):                    # Funcion principal
    z = x**2 - y**2
    return z

x0 = np.linspace(-10, 10, 1000)
x1 = np.linspace(-10, 10, 1000)
fig = plt.figure()                          # complementacion de la grafica
ax = plt.subplot(111, projection="3d")      # Grafica en 3d
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

lr = 0.1                        # Tasa de aprendizaje
x1_list = []
y1_list = []
z_list = []
thetay = 0                      # Posicion en el eje x
thetax = -10                    # Posicion en el eje y

def dxf(x):                     # Derivada parcial de x
    y = 2*x
    return y

def dyf(y):                     # Derivada parcial de y
    x = -2*y
    return x

for _ in range(30):            
    x1_list.append(thetax)      
    y1_list.append(thetay)
    z_list.append(f(thetax, thetay))
    thetax = thetax - lr * dxf(thetax)       # Optimizacion de las posiciones
    thetay = thetay - lr * dyf(thetay)       # al minimo local
    print(f"iteracion {_+1}: {round(thetax, 2), round(thetay, 2)}")

print(f"Minimo local: {round(thetax, 2), round(thetay, 2)}")
x0, x1 = np.meshgrid(x0, x1)
z = f(x0, x1)
ax.plot_surface(x0, x1, z, rstride=5, cstride=5, cmap="gist_stern")
ax.plot(x1_list, y1_list, z_list, "bo--")