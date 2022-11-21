### Sieci neuronowe

“Zaimplementuj perceptron dwuwarstwowy. Naucz go reprezentować funkcję J : [-5,5] → R, daną
wzorem: J(X) = sin(X × pierwiastek(p[1]+1)) + cos(X × pierwiastek(p[2]+1)), gdzie p[1] i p[2] to najmłodsze
cyfry numerów indeksów wykonawców. Zakładamy, że jest to zagadnienie aproksymacji funkcji na
zbiorze nieskończonym, tj. nie mamy dostępu do całości zbioru, za to mamy generator, który generuje
kolejne próbki funkcji. Po nauczeniu sieci należy wygenerować zbiór testujący i określić dokładność
aproksymacji na tym zbiorze.”

Perceptron dwuwarstwowy jest szczególnym przypadkiem sieci neuronowej która ma tylko dwie warstwy
(ukrytą i wyjściową). W warstwie ukrytej może być dowolna liczba neuronów z dowolną, ale jednakową
liczbą wejść. W warstwie wyjściowej powinno być tyle neuronów, ile powinno być wyjść i tyle wejść u
każdego neuronu, ile jest neuronów w warstwie ukrytej.
Na jakość przewidywania wartości funkcji za pomocą perceptronu dwuwarstwowego wpływa:
1) Ilość neuronów w warstwie ukrytej. Im jest ich więcej tym mniej jest wartość funkcji błędu
2) Ilość iteracji sieci (w ciągu każdej iteracji sieć przechodzi przez każdy element zbioru testującego i
poprawia wartości wag neuronów zgodnie z zaimplementowaną metodą poprawiania wag). Czyli im
więcej jest iteracji, tym więcej razy sieć będzie poprawiać wartości wag i tym lepiej się nauczy.
3) Wielkość zbioru trenującego. Im większy jest zbiór trenujący, tym więcej obszarów funkcji sieć będzie
miała możliwość przebadać, czyli im bardziej skomplikowana jest funkcja, tym większy powinien być
zbiór trenujący.

Ale ustawienie dla tych parametrów największe jakie się da wartości też nie zawsze ma sens, ponieważ:
1) W pewnym momencie zwiększenie ilości neuronów w warstwie ukrytej przestaje dawać znaczący
rezultat w osiągnięciu minimalnej wartości błędu
2) To może doprowadzić do przeuczenia sieci.
3) Zazwyczaj zwiększenie tych parametrów znacznie zwiększa czas trenowania sieci.

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/two-layer_perceptron/imgs/table_1.png" />
<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/two-layer_perceptron/imgs/table_2.png" />


Wyniki w postaci wykresów (odpowiadające kolejnym wartościam wyróżnionych w tabeli parametrów)

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/two-layer_perceptron/imgs/result_1.png" width="600" height="300" />
<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/two-layer_perceptron/imgs/result_2.png" width="600" height="300" />
<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/two-layer_perceptron/imgs/result_3.png" width="600" height="300" />
