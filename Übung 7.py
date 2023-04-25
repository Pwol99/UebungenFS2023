#Aufgabe 1
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(-100, 100, 1000)
y = np.random.uniform(-100, 100, 1000)
plt.scatter(x, y, c=np.random.rand(1000,3))
plt.title('1000 zufällige Punkte')
plt.xlabel('X-Koordinate')
plt.ylabel('Y-Koordinate')
plt.show()


#Aufgabe 2

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.exp(-x**2) * np.sin(y)

# Erstelle Arrays mit x- und y-Koordinaten
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Erstelle Gitterpunkte mit np.meshgrid
X, Y = np.meshgrid(x, y)

# Werte die Funktion an den Gitterpunkten aus
Z = f(X, Y)

# Plotten Sie das Ergebnis
plt.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower')
plt.colorbar()
plt.title('f(x, y) = exp(-x^2) * sin(y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

