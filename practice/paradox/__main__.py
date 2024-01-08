from MontyHall import *
from Birhdays import *
if __name__ == '__main__':
    paradoxn = int(input("Какую задачу вы хотите решить?\n"
                         "1. Проблема Монти Холла\n"
                         "2. Задача о днях рождениях\n"))

    num_simulations = int(input("Введите количество симуляций: "))

    if paradoxn == 1:
        monty_hall_paradox(num_simulations)
    elif paradoxn == 2:
        print("Вероятность совпадения дней рождения:", birthday_paradox(num_simulations))