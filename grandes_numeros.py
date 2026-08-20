import numpy as np

rng = np.random.default_rng(seed = 91)

cara = 0
cruz = 0

for i in range(10000):

    random = rng.random()
    if(random > 0.5):
        cara = cara + 1

    elif (random <= 0.5):
        cruz = cruz + 1


print("numero de caras: ", cara)
print("numero de cruz: ", cruz)

# generar poblacion

iteraciones = 10
vector = []

for i in range(iteraciones):
    random = rng.random()

    valor = 1 + random * (1 - (-1))

    vector.append(valor)

print("vector obtenido: ", vector)

# funcion para quicksort
def QuickSort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] 

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return QuickSort(left) + middle + QuickSort(right)

# obtener vector ordenado
print("vector ordenado: ")
vector_ordenado = QuickSort(vector)
print(vector_ordenado)

# funncion para busqueda lineañ
def LinearSearch(arr):

    for i in range(len(arr)):
        if(i == 7):
            return arr[i]

    return -1

# imprimir valor devuelto por la busqueda
print(LinearSearch(vector_ordenado))

