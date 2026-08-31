import numpy as np
import matplotlib.pyplot as plt

# alpha = lr (learning rate)
# no es bueno que el learning rate sea tan grande ya que puede comportarse de forma muy greedy o agresiva, por lo que no le permitimos al algoritmo explorar.
def Gradiente(x, y, Lr=0.01, iter = 1000):
    n = len(y)
    x1 = 0.0 # se le pone 0.0 para especificar que el valor es un flotante.
    x2 = 0.0

    historial_costo = []

    for i in range(iter):
        # cambiar función objetivo
        y_pred = x1*x**2 + x2*x + 2 # función cuadrática
        costo = 1 / n * np.sum((y - y_pred)**2) # cálculo error cuadrático medio
        historial_costo.append(costo)

        # cambiar derivadas
        x1_derivada = (-2/n) * np.sum((x**2)*(y-y_pred)) # derivadas
        x2_derivada = (-2/n) * np.sum(x*(y-y_pred))
        x1 = x1 - Lr * x1_derivada
        x2 = x2 - Lr * x2_derivada

    return x1, x2, historial_costo

np.random.seed(42)

X = np.array([1,2,3,4,5], dtype = float)
Y = np.array([5,7,9,11,13], dtype = float)

x1_opt, x2_opt, costo_hist = Gradiente(X, Y, Lr = 0.0002, iter=300)

# hay que escribir con acentos incluso si es en el código
print(f"Valor óptimo (x1): {x1_opt:.4f}")
print(f"Valor óptimo (x2): {x2_opt:.4f}")
print(f"Costo final: {costo_hist[-1]:.6f}")

# agregar gráficos
plt.plot(costo_hist, marker = "o", markersize = 3)
plt.xlabel("Iteraciones")
plt.ylabel("Costo")
plt.title("Gradiente")
plt.grid(True)

plt.show()