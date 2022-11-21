# Zaimplementuj perceptron dwuwarstwowy.
# Naucz go reprezentować funkcję J : [-5,5] → R,
# daną wzorem: J(x) = sin(x*pierwiastek(p[1]+1))+cos(x*pierwiastek(p[2]+1)),
# gdzie p[1] i p[2] to najmłodsze cyfry numerów indeksów wykonawców.
# Zakładamy, że jest to zagadnienie aproksymacji funkcji na zbiorze
# nieskończonym, tj. nie mamy dostępu do całości zbioru, za to mamy generator,
# który generuje kolejne próbki funkcji. Po nauczeniu sieci należy wygenerować
# zbiór testujący i określić dokładność aproksymacji na tym zbiorze.


import math as m
import matplotlib.pyplot as plt
import numpy as np


down_limit, up_limit = -5, 5
p1, p2 = 3, 2
train_data_size, test_data_size = 1500, 300
neuron_number = 40
train_iterations = 500
learn_coeff = 0.01
n = 3 # liczba uruchomień analizy algorytmu


def generate_x(down_limit, up_limit):
    # generacja wartości wejściowych sieci
    return np.random.uniform(down_limit, up_limit)


def function(x):
    # funkcja do aproksymacji
    return m.sin(x * (m.sqrt(p1 + 1))) + m.cos(x * (m.sqrt(p2 + 1)))


def generate_test_set(down_limit, up_limit, size):
    # generacja danych
    test_set = {}
    for _ in range(size):
        x_test = generate_x(down_limit, up_limit)
        y_test = function(x_test)
        test_set.update({x_test: y_test})
    return list(test_set.keys()), list(test_set.values())


def activation_func(x):
    # funkcja aktywacji - hiperboliczny tangens
    return np.tanh(x)


def deriv_activation_func(x):
    # pochodna funkcji aktywacji
    return (((np.cosh(x)) ** 2) - ((np.sinh(x)) ** 2)) / ((np.cosh(x)) ** 2)



class Two_layer_perceptron:

    def __init__(self, hidden_neurons_number):
        self.hidden_layer_weights = np.float64(np.random.normal(0, 1, (2, hidden_neurons_number)))
        self.output_layer_weights = np.float64(np.random.normal(0, 1, (hidden_neurons_number + 1, 1)))
        self.hidden_layer_result, self.output_layer_result, self.hidden_layer_before_activation = None, None, None

    def predict(self, x):
        inputs = np.append(x, 1)
        self.hidden_layer_before_activation = np.dot(inputs,self.hidden_layer_weights)
        self.hidden_layer_result = activation_func(self.hidden_layer_before_activation)
        self.output_layer_result = np.dot(np.append(self.hidden_layer_result, 1),self.output_layer_weights)
        return self.output_layer_result

    def train(self, data_x, data_y, iterations, learn_coeff):

        for iteration in range(iterations):
            iteration_error = []
            for x, y in zip(data_x, data_y):

                inputs = np.append(x, 1)
                predicted_y = self.predict(x)

                # funkcja błędu
                error = (y - predicted_y) ** 2
                iteration_error.append(error)

                # pochodna funkcji błędu
                error_function_derivative = -2 * (y - predicted_y)

                # obliczenie pochodnych dla warstwy wyjściowej
                output_layer_derivative = list(error_function_derivative * np.append(self.hidden_layer_result, 1))
                output_layer_derivative = np.array([output_layer_derivative]).T

                # obliczenie pochodnych dla warstwy ukrytej
                hidden_layer_derivative = error_function_derivative * self.output_layer_weights[:-1] * np.array([list(inputs)]) * deriv_activation_func(np.array([list(self.hidden_layer_result)]).T)
                hidden_layer_offset_derivative = error_function_derivative * self.output_layer_weights[:-1] * np.array([list(inputs)]) * deriv_activation_func(np.array([list(self.hidden_layer_before_activation)]).T)
                hidden_layer_derivative = hidden_layer_derivative.T
                hidden_layer_derivative[1] = hidden_layer_offset_derivative.T[1]

                # aktualizacja wag i offsetów

                # aktualizacja dla warstwy ukrytej
                self.hidden_layer_weights -= learn_coeff * hidden_layer_derivative

                # aktualizacja dla warstwy wyjściowej
                self.output_layer_weights -= learn_coeff * output_layer_derivative


            if iteration % 10 == 0:
                print(f"Iteration: {iteration}, average error of last 10 iterations: {np.mean(iteration_error)}")
    
    def check(self, test_x, test_y):
        network_results = []
        for element in test_x:
            network_results.append(self.predict(element))
        plt.plot(test_x, test_y, 'o', color='red')
        plt.plot(test_x, network_results, 'o', color='blue')
        plt.show()

    def check_error(self, test_x, test_y):
        percent_error = []
        for i in range(len(test_x)):
            percent_error.append(100 * abs(((test_y[i] - self.predict(test_x[i])[0])) / test_y[i]))
        return np.mean(percent_error), np.std(percent_error), round(max(percent_error), 3), round(min(percent_error), 3)


def analyze_network_results(network, n):
    print(f'Liczba neuronów: {neuron_number}, liczba iteracji: {train_iterations}, rozmiar zbioru uczącego: {train_data_size}, rozmiar zbioru testującego: {test_data_size}, współczynnik beta: {learn_coeff}')
    for _ in range(n):
        test_data = generate_test_set(down_limit, up_limit, test_data_size)
        result = network.check_error(test_data[0], test_data[1])
        print(f'Procentowy błęd aproksymacji: średnia: {result[0]}, odchylenie standardowe: {result[1]}, max wartość: {result[2]}, min wartość: {result[3]}')



train_data = generate_test_set(down_limit, up_limit, train_data_size)
test_data_1 = generate_test_set(down_limit, up_limit, test_data_size)
test_data_2 = generate_test_set(down_limit, up_limit, test_data_size)

network = Two_layer_perceptron(neuron_number)
network.train(train_data[0], train_data[1], train_iterations, learn_coeff)
network.check(test_data_1[0], test_data_1[1])
analyze_network_results(network, n)
