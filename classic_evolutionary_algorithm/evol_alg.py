# realizacja klasycznego algorytmu ewolucyjnego
# selekcja turniejowa, jednorodne krzyzowanie, sukcesja generacyjna
# badana funkcja (minimalizacja) - funkcja numer 6 z benchmarku CEC2005


import optproblems
import optproblems.cec2005
import numpy as np
import random


# ograniczenia do x
x_up_limit = 100.0
x_down_limit = -100.0

# parametry algorytmu
variables = 10
population_size = 1000
budget = variables * 10000
iterations = budget / population_size
sigma = 0.2

# ilosc razy uruchamiania algorytmu
attempts = 25

# funkcja
f6 = optproblems.cec2005.F6(10)


def generation(population_size):

    population = []
    for _ in range(population_size):
        x_coordinates = []
        for _ in range(variables):
            x_coordinates.append(np.random.randint(x_down_limit, x_up_limit))          
        population.append(x_coordinates)
    return population


def population_rating(population_size, population):

    population_results = []
    for i in range(population_size):
        individual = optproblems.base.Individual(population[i])
        f6.evaluate(individual)
        population_results.append(round(individual.objective_values, 1))
    return population_results


def selection(population_size, population, population_results):

    selected = []
    for _ in range(population_size):
        opponent_1, opponent_2 = random.randint(0,population_size-1), random.randint(0,population_size-1)
        if population_results[opponent_1] < population_results[opponent_2]:
            selected.append(population[opponent_1])
        else:
            selected.append(population[opponent_2])
    return selected


def crucifixion(population_size, selected):

    population = []
    crucifixion_factors = []
    for _ in range(population_size):
        crucifixion_factors.append(random.uniform(0, 1))

    for _ in range(0, int(len(selected))):
        i, j = random.randint(0,len(selected)-1), random.randint(0,len(selected)-1)
        if crucifixion_factors[i] < 0.7:
            while j == i:
                j = random.randint(0,len(selected)-1)
            child = []
            for k in range(len(selected[0])):
                child.append(random.choice([selected[i][k], selected[j][k]]))
            population.append(child)
        else:
            population.append(selected[i])
    return population


def mutation(population):

    for i in range(len(population)):
        
        for j in range(len(population[i])):
            population[i][j] = population[i][j] + np.random.normal(0, sigma)
            if population[i][j] > x_up_limit:
                population[i][j] = x_up_limit
            if population[i][j] < x_down_limit:
                population[i][j] = x_down_limit
    return population


def choose_the_best(population, population_results):
    best_solution, best_value = population[0], population_results[0]
    for i in range(population_size):
        if population_results[i] < best_value:
            best_solution, best_value = population[i], population_results[i]
    return best_solution, best_value


def evolutionary_alg(x_up_limit, x_down_limit, variables, population_size, iterations, sigma):

    # generacja populacji
    population = generation(population_size)

    # ocena populacji
    population_results = population_rating(population_size, population)

    # petla algorytmu
    for _ in range(iterations):

        # selekcja turniejowa
        selected = selection(population_size, population, population_results)

        # krzyzowanie jednorodne
        population = crucifixion(population_size, selected)

        # mutacja
        population = mutation(population)

        # ocena populacji
        population_results = population_rating(population_size, population)

    # wartosc najlepszego osobnika
    return choose_the_best(population, population_results)


# uruchomienie analizy algorytmu
def start_alg_analysis(attempts):
    results = []
    for _ in range(attempts):
        results.append(evolutionary_alg(x_up_limit, x_down_limit, variables, population_size, iterations, sigma)[1])
        
    print('Srednia wartosc: ', sum(results)/attempts)
    print('Odchylenie standardowe: ', np.std(results))
    print('Maksymalna wartosc: ', max(results))
    print('Minimalna wartosc: ', min(results))


start_alg_analysis(attempts)
