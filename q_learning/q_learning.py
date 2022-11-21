# Zaimplementuj algorytm Q-Learning i użyj go do wyznaczenia polityki
# decyzyjnej dla problemu FrozenLake8x8-v0:
# https://gym.openai.com/envs/FrozenLake8x8-v0/
# W problemie chodzi o to, aby agent przedostał się przez zamarznięte
# jezioro z pozycji S do pozycji G unikając punktów H. Symulator dla tego
# problemu można pobrać z podanej strony lub napisać własny o takiej samej funkcjonalności.
# Jak zmienia się suma zdobywanych kar w funkcji numeru epoki (epizodu)?
# Oprócz zbadania domyślnego sposobu nagradzania proszę zaproponować własny
# system nagród i kar i porównać osiągane wyniki z wynikami systemu domyślnego.

import random
from frozen_lake import *
import numpy as np


# współczynnik, reprezentujący stopień, w jakim zmeniają
# się wartości w tabeli uczenia się podczas każdej iteracji
learning_rate = 0.01

# współczynnik definiujący które nagrody są preferowane,
# im bliżej jest do jedynki tym bardziej są preferowane przyszłe nagrody,
# im bliżej jest do zera tym bardziej są preferowane natychmiastowe nagrody
discount_factor = 0.95

# współczynnik definiujący balans pomiędzy eksploracją a eksploatacją
# czyli pomiędzy badaniem środowiska a wykorzystaniem już zdobytej wiedzy
exploration_limiter = 0.2

# iteracji uczenia się
training_iterations = 25000

test_iterations, alg_iterations = 25, 100

class Q_learning_for_frozen_lake():

    def __init__(self, learning_rate, discount_factor, exploration_limiter, training_iterations, cur_map="4x4"):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.training_iterations = training_iterations
        self.exploration_limiter = exploration_limiter
        self.game = FrozenLakeEnv(map_name=cur_map)

        # tabela która pozwala uczyć się na podstawie otrzymywanych nagród
        self.q_values = []
        for _ in range(self.game.nS): # ile jest wszystkich możliwych stanów w tym środowisku
            temp = []
            for _ in range(self.game.nA): # ile jest wszystkich możliwych ruchów w tym środowisku
                temp.append(0)
            self.q_values.append(temp)


    def train(self, custom_reward):

        total_reward = 0

        for iteration in range(training_iterations):

            current_observation = self.game.reset() # resetuje środowisko
            reward = 0
            done = False

            # dopuki gra nie dojdzie do stanu terminalnego
            while not done:
                exploration_probability = random.uniform(0, 1)
                if  exploration_probability < self.exploration_limiter:
                    move = random.randint(0, self.game.nA - 1)
                else:
                    move = self.q_values[current_observation].index(max(self.q_values[current_observation]))

                # wykonanie wybranego ruchu, zwraca obserwację, nagrodę, czy nowy stan jest terminalnym i dodatkową informację
                next_observation, reward, done, _ = self.game.step(move)

                # jeżeli wykorzystywana jest wprowadzona funkcja nagradzania
                if custom_reward:
                    if reward:
                        reward = 100
                    elif done and not reward:
                        reward = -100
                    else:
                        reward = -1

                # odnowienie wartości w tablicy
                prev_q_value = self.q_values[current_observation][move]
                update_q_value = prev_q_value + self.learning_rate * (reward + self.discount_factor * max(self.q_values[next_observation]) - prev_q_value)
                self.q_values[current_observation][move] = update_q_value
                current_observation = next_observation

            total_reward += reward

            if iteration == 5 or iteration == 10 or iteration == 100:
                print(f"Numer iteracji trenującej: {iteration}, suma nagród za ostatnie {iteration} iteracji: {total_reward/iteration}")

            if iteration % 1000 == 0 and iteration != 0:
                print(f"Numer iteracji trenującej: {iteration}, suma nagród za ostatnie 1000 iteracji: {total_reward/1000}")
                total_reward = 0


    def test(self, test_iterations, alg_iterations):
        total_rewards = []
        total_steps = 0
        total_reward = 0
        for _ in range(test_iterations):
            total_reward = 0
            for _ in range(alg_iterations):
                current_observation = self.game.reset()
                steps, reward =  0, 0
                done = False
                
                while not done:
                    move = self.q_values[current_observation].index(max(self.q_values[current_observation]))
                    current_observation, reward, done, _ = self.game.step(move)
                    steps += 1
                total_steps += steps
                total_reward += reward
            total_rewards.append(total_reward)

        print(f"Resultat {alg_iterations} gier:")
        print(f"Średnia liczba ruchów w grze: {total_steps / (alg_iterations * test_iterations)}")
        print(f"Gier które zakończyły się sukcesem: {total_reward}")
        print('Liczba uruchomień agorytmu: ', test_iterations)
        print('Srednia wartosc: ', round(np.mean(total_rewards), 2))
        print('Odchylenie standardowe: ', round(np.std(total_rewards), 2))
        print('Maksymalna wartosc: ', round(max(total_rewards), 2))
        print('Minimalna wartosc: ', round(min(total_rewards), 2))


algorithm = Q_learning_for_frozen_lake(learning_rate, discount_factor, exploration_limiter, training_iterations)
algorithm.train(False)
algorithm.test(test_iterations, alg_iterations)
algorithm.train(True)
algorithm.test(test_iterations, alg_iterations)
