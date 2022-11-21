# realizacja stochastycznego algorytmu wspinaczkowego
# badana funkcja - Z(X, Y) = X^2 + 5 * (Y^2)
# kod jest napisany w taki sposób żeby było łatwo
# zmienić ograniczenia współrzednych oraz funkcję

# importy potrzebnych modułów
import random
import numpy as np
import matplotlib.pyplot as plt

# ograniczenia do x i y
x_up_limit = 20.0
y_up_limit = 20.0
x_down_limit = -20.0
y_down_limit = -20.0

# funkcja
z = 'X**2 + 5 * (Y**2)'

# ilość razy uruchamiania algorytmu
attempts = 50


def stohastic_climb_alg(z, x_up_limit, y_up_limit, x_down_limit, y_down_limit):
    # wybierane losowo początkowe współrzedne punktu roboczego
    x, y = np.random.randint(x_down_limit, x_up_limit), np.random.randint(y_down_limit, y_up_limit)

    # listy do współrzędnych odwiedzonych punktów
    x_coordinates = [x]
    y_coordinates = [y]

    # cykl algorytmu
    for _ in range(100):
        # generacja współrzędnych sąsiednego punktu
        neiborhood = np.random.multivariate_normal((x, y), [[x, y],[x, y]])
        new_x, new_y = neiborhood[0], neiborhood[1]

        # sprawdzenie czy wspórzędne punktu sąsiedniego nie wyszli poza ustalone granicy
        if new_x < x_down_limit or new_x > x_up_limit or new_y < y_down_limit or new_y > y_up_limit:
            continue

        # badanie czy punkt sąsiedni ma lepszą wartość funkcji celu od puktu roboczego
        if eval(z, {'X': x, 'Y': y}) > eval(z, {'X': new_x, 'Y': new_y}):
            # punkt sąsiedni staje się nowym punktem roboczym
            x = new_x
            y = new_y
            # dodanie wspórzędnych nowego punktu roboczego do listy odwiedzonych wspórzędnych
            x_coordinates.append(x)
            y_coordinates.append(y)

    return eval(z, {'X': x, 'Y': y}), x_coordinates, y_coordinates


def draw_plot(z, x_up_limit, y_up_limit, x_down_limit, y_down_limit, x_coordinates, y_coordinates):
    # rysowanie wykresu funkcji
    # i wizualizacja odwiedzonych punktów
    xlist = np.linspace(x_down_limit, x_up_limit)
    ylist = np.linspace(y_down_limit, y_up_limit)
    X, Y = np.meshgrid(xlist, ylist)
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, eval(z, {'X': X, 'Y': Y}))
    ax.plot(x_coordinates, y_coordinates, 'o', color='white', linewidth=1.0)
    ax.set_title('Example of visualization of stohastic climbing algorithm')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()


# uruchomienie analizy algorytmu
def start_alg_analysis(attempts):
    results = []
    for _ in range(attempts):
        results.append(stohastic_climb_alg(z, x_up_limit, y_up_limit, x_down_limit, y_down_limit)[0])

    print('Średnia wartość: ', sum(results)/attempts)
    print('Odchylenie standardowe: ', np.std(results))
    print('Maksymalna wartość: ', max(results))
    print('Minimalna wartość: ', min(results))

    for el in enumerate(results):
        results[el[0]] = abs(el[0])

    print('Najlepsza wartość: ', min(results))

    random_result = stohastic_climb_alg(z, x_up_limit, y_up_limit, x_down_limit, y_down_limit)
    draw_plot(z, x_up_limit, y_up_limit, x_down_limit, y_down_limit, random_result[1], random_result[2])


start_alg_analysis(attempts)
