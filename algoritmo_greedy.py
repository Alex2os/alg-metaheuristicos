import numpy as np

rng = np.random.default_rng() # se le pone semilla para que los resultados no sean random o aleatorios. sin semilla es aleatorio cada vez

# inicializar poblacion
iteraciones = 30
vector = []

for i in range(iteraciones):
    random = rng.random()

    valor = -1 + random * (1 - (-1))

    vector.append(valor)

print("vector obtenido: ", vector)

# algoritmo greedy (tipo migajero. agarra el primer resultado que se encuentre)
x_best = 0

pop = len(vector)

for i in range(pop):
    print(vector[i])
    if vector[i] >= 0.9:
        x_best = vector[i]
        break

print("x_best obtenido:", x_best)