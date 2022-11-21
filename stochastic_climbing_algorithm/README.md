### Realizacja stochastycznego algorytmu wspinaczkowego

Algorytm wspinaczkowy jest rodzajem algorytmu zachłannego, to znaczy, że na każdym etapie
podejmuje się lokalnie optymalna decyzja zakładając, że ostateczna decyzja również będzie optymalna.

Na pierwszym etapie algorytmu generuje się pierwszy stan jako punkt roboczy i on dodaje się do zbioru
punktów odwiedzonych. Współrzędne tego punktu mogą zostać wygenerowany losowo. Kolejnym
etapem jest cykl, w którym zostaje wygenerowany zbiór punktów sąsiednich do punktu roboczego i dla
każdego z nich oblicza się wartość funkcji celu. Potem z punktów sąsiednich wybieramy ten u którego
wartość funkcji celu okazała się lepsza (większą czy mniejsza, zależy od tego czy szukamy maksimum czy
minimum) od wartości funkcji celu punktu roboczego. Jeżeli taki sąsiad znalazł się to on staję się nowym
punktem roboczym, zostaje dodany do zbioru punktów odwiedzonych i odbywa się kolejna iteracja
cyklu. Natomiast jeżeli taki sąsiad się nie znalazł, to oznacza, że punkt, który teraz jest zaznaczony jako
roboczy jest rozwiązaniem i algorytm skończył swoje działanie.

Stochastyczny algorytm wspinaczkowy różni się od zwykłego algorytmu wspinaczkowego tym, że zamiast
całego sąsiedztwa punktu roboczego generowany jest tylko jeden sąsiad za pomocą losowania bez
zwracania. Jeżeli ten sąsiad jest lepszy to on staję się nowym punktem roboczym, jeżeli nie to odbywa
się kolejne losowanie. Dla losowania jest używana specjalna funkcja x + N(0, sigma), gdzie x to atualna
współrzędna, N to rozkład normalny, sigma to wartość dostosowana do tego żeby rozkład normalny
losował takie liczby żeby algorytm potrafił znaleźć rozwiązanie.

Kolejne kroki algorytmu:
- Wybierane losowo początkowe współrzędne punktu roboczego
- Tworzenie list do współrzędnych odwiedzonych punktów, dodanie do nich punktu roboczego
- Cykl:
  - Losowy wybór współrzędnej do zmiany
  - Generacja współrzędnych sąsiedniego punktu za pomocą funkcji rozkładu normalnego i współrzędnych punktu roboczego
  - Badanie czy punkt sąsiedni ma lepszą wartość funkcji celu od puktu roboczego
  - Jeżeli wartość funkcji celu punktu sąsiedniego jest lepsza:
    - Punkt sąsiedni staje się nowym punktem roboczym
    - Dodanie współrzędnych nowego punktu roboczego do list odwiedzonych współrzędnych

Zaletą wyżej wspomnianych algorytmów jako algorytmów zachłannych jest to, że oni są łatwe w
realizacji, natomiast wadą jest to, że dla niektórych funkcji oni mogą znaleźć tylko minimum lub
maksimum lokalny i na tym się zatrzymać, i z tego powodu rzadko są używane w praktyce.

Przykłady działania algorytmu:

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/stochastic_climbing_algorithm/imgs/result_1.png" />

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/stochastic_climbing_algorithm/imgs/result_2.png" />

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/stochastic_climbing_algorithm/imgs/result_3.png" />

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/stochastic_climbing_algorithm/imgs/result_4.png" width="500" height="450" />

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/stochastic_climbing_algorithm/imgs/result_5.png" width="500" height="450" />

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/stochastic_climbing_algorithm/imgs/result_6.png" width="500" height="450"/>
