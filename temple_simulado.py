import numpy as np
import math
import random
import matplotlib.pyplot as plt

# definición de funciones

# función peaks
def peaks(x, y):
    return 3*(1-x)**2 * np.exp(-(x**2) - (y+1)**2) - 10*(x/5 - x **3 - y **5 ) * np.exp(-x**2 - y**2) - 1/3*np.exp(-(x+1)**2 - y **2)
# return x**2+y**2

# función objetivo que toma un vector [x,y]
def objective_function(position):
    x, y = position
    return peaks(x,y) # minimización

# límites del espacio de búsqueda
lower_bound = np.array([-3, -3])
upper_bound = np.array([3,3])

# generar vecino dentro de los limites
def neighbor(position, step_size = 0.5):
    new_position = position + np.random.uniform(-step_size, step_size, size = 2)
    return np.clip(new_position, lower_bound, upper_bound) # restringe a los límites

# probabilidad de aceptación
def acceptance_probability(current_energy, neighbor_energy, temperature):
    if neighbor_energy < current_energy:
        return 1.0
    return math.exp((current_energy - neighbor_energy) / temperature)

# simulated annealing con historial de posiciones
def simulated_annealing(initial_solution, initial_temperature,
                        cooling_rate, max_iterations):

    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    best_solution = current_solution
    best_energy = current_energy

    temperature = initial_temperature
    path = [current_solution.copy()] # guarda la trayectoria

    for iteration in range(max_iterations):
        new_solution = neighbor(current_solution)
        new_energy = objective_function(new_solution)
        if acceptance_probability(current_energy, new_energy, temperature) > random.random():
            current_solution = new_solution
            current_energyu = new_energy
            path.append(current_solution.copy())

        