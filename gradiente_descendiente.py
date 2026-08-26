import numpy as np
import matplotlib.pyplot as plt

# alpha = lr (learning rate)
# no es bueno que el learning rate sea tan grande ya que puede comportarse de forma muy greedy o agresiva, por lo que no le permitimos al algoritmo explorar.
def Gradiente(x, y, Lr=0.01, iter = 1000):
    n = len(y)
    m = 0.0 # se le pone 0.0 para especificar que el valor es un flotante.
    b = 0.0

    historial_costo = []

    for i in range(iter):
        # cambiar funcion objetivo
        y_pred = m * x + b
        costo = 1 / n * np.sum(x * (y - y_pred)**2) # calculo error cuadratico medio
        historial_costo.append(costo)

        # cambiar derivadas
        dm = (-2/n) * np.sum(x*(y-y_pred)) # derivadas
        db = (-2/n) * np.sum(y-y_pred)
        m = m - Lr * dm
        b = b - Lr * db

    return m, b, historial_costo

np.random.seed(42)

X = np.array([1,2,3,4,5], dtype = float)
Y = np.array([5,7,9,11,13], dtype = float)

m_opt, b_opt, costo_hist = Gradiente(X, Y, Lr = 0.005, iter=500)

# hay que escribir con acentos incluso si es en el código
print(f"Pendiente óptima (m): {m_opt:.4f}")
print(f"Intersección óptima (b): {b_opt:.4f}")
print(f"Costo final: {costo_hist[-1]:.6f}")

# agregar graficos
plt.plot(costo_hist, marker = "o", markersize = 3)
plt.xlabel("iteracion")
plt.ylabel("mejor fitness encontrado")
plt.title("Busqueda aleatoria en f(x) = 5cos(x)+cos(5x)")
plt.grid(True)

plt.show()