import random
import numpy as np
import matplotlib.pyplot as plt

def Ob_f(x):
    return np.power((8 * np.sin(x) + (1 / np.cos(2*x))), 2)

# 8np.sen(x) + np.sec(2x) al cuadrado 

# hiperparametros
num_iter = 100
rango_min = -10
rango_max = 10

mejor_x = None
mejor_fitness = float("inf")
mejores = []

for i in range(num_iter):
    x = random.uniform(rango_min, rango_max)
    f = Ob_f(x)
    if(f < mejor_fitness): # para maximizar o minimizar simplemente cambiamos el signo de este if.
        mejor_x = x
        mejor_fitness = f
    mejores.append(mejor_fitness)

print("Mejor valor encontrado")
print("x=", mejor_x)
print("f(x)=", mejor_fitness)

plt.plot(mejores, marker = "o", markersize = 3)
plt.xlabel("iteracion")
plt.ylabel("mejor fitness encontrado")
plt.title("Busqueda aleatoria en f(x) = 5cos(x)+cos(5x)")
plt.grid(True)

plt.show()