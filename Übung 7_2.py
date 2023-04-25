#Aufgabe 7.2

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.exp(-x**2) * np.sin(y)

# Erstelle Arrays mit x- und y-Koordinaten
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

plt.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower')
plt.colorbar()
plt.title('f(x, y) = exp(-x^2) * sin(y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()