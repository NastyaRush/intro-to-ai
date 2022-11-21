### Realizacja klasycznego algorytmu ewolucyjnego

Sprawność algorytmu genetycznego zależy od tego jak są zaimplementowane jego poszczególne części (selekcja,
operatory genetyczne, sukcesja). W danej realizacji używa się selekcja turniejowa która jest dobrym rozwiązaniem
ponieważ wybiera dobrych osobników i jednocześnie daję szansę przeżyć gorszym które potem mogliby sprowadzić
do badania oddalonych obszarów; krzyżowanie jednorodne i mutacja występują jako operatory genetyczne,
krzyżowanie jednorodne nie jest dobrym rodzajem krzyżowania ponieważ może doprowadzić do zgubienia
odnalezionych dobrych rozwiązań; sukcesja generacyjna jest dobrą metodą, może spowodować że do populacji
trafią źle osobniki, ale mianowicie oni w skutku mogą doprowadzić do znalezienia optimum globalnego.
Także otrzymany rezultat w dużej mierze zależy od początkowo wygenerowanych wartości, szczególnie przy
skomplikowanym problemie, to wyjaśnia, dlaczego te same parametry algorytmu mogą dać wyniki różniące się o
kilka razy.

Mały zasięg mutacji spowoduje to, że algorytm będzie robić małe kroki niewystarczająco badając różne obszary
przestrzeni przeszukiwań i z tego powodu będzie szukał lepszych rozwiązań w bardzo wolny sposób natomiast
bardzo duży zasięg mutacji spowoduje to, że algorytm będzie robić bardzo duże kroki i w taki sposób może oddalić
się od znalezionego dobrego rozwiązania.

Poniższa tabela reprezentuje, jak zmieniają się wyniki algorytmu w zależności od parametru sigma (sigma to jest
parametr, który jest używany do realizacji mutacji jako parametr rozkładu normalnego, czyli gdzie będzie
znajdować się wygenerowany punkt sąsiedni). Z tabeli widać, że należy zwrócić szczególną uwagę na wybór tego
parametru, ponieważ tylko wartości w określonym przedziale dają sensowne wyniki.

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/classic_evolutionary_algorithm/imgs/result_1.png" />

Przykłady rezultatów działania algorytmu:

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/classic_evolutionary_algorithm/imgs/result_2.png" width="600" height="300" />
