### Uczenie się ze wzmocnieniem

“Zaimplementuj algorytm Q-Learning i użyj go do wyznaczenia polityki decyzyjnej dla problemu FrozenLake8x8-
v0:
https://gym.openai.com/envs/FrozenLake8x8-v0/

W problemie chodzi o to, aby agent przedostał się przez zamarznięte jezioro z pozycji S do pozycji G unikając
punktów H. Symulator dla tego problemu można pobrać z podanej strony lub napisać własny o takiej samej
funkcjonalności.

Jak zmienia się suma zdobywanych kar w funkcji numeru epoki (epizodu)?
Oprócz zbadania domyślnego sposobu nagradzania proszę zaproponować własny system nagród i kar i porównać
osiągane wyniki z wynikami systemu domyślnego.”

Domyślny system kar i nagród: -0 za kolejny ruch, +1 za osiągnięcie celu.

Wprowadzony system kar i nagród: -1 za kolejny ruch, +100 za osiągnięcie celu, -100 za osiągnięcie stanu
terminalnego który nie jest docelowym. Jak widać z tabeli z wynikami ten system okazał się trochę lepszy niż
domyślny i z takim systemem algorytm szybciej się uczy.

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/q_learning/imgs/table_1.png" />

Jak widać z tabeli z sumami nagród, z kolejnymi iteracjami uczenia się zwiększa się liczba otrzymanych nagród,
ponieważ algorytm stara się omijać “pułapki”, robić jak najmniej kroków i zbliżać się do punktu docelowego.

Także dla lepszego uczenia się trzeba odpowiednio dobrać parametry algorytmu.

Przykładowy wynik uruchomienia algorytmu:

Ocenianie domyślne:

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/q_learning/imgs/result_1.png" />

Ocenianie wprowadzone:

<img src="https://raw.githubusercontent.com/NastyaRush/intro-to-ai/main/q_learning/imgs/result_2.png" />
