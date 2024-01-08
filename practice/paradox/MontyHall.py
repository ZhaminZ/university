import random

def monty_hall_paradox(simulations):
    stay_wins = 0
    switch_wins = 0

    for _ in range(simulations):
        doors = [0, 0, 1]
        random.shuffle(doors)
        player_choice = random.randrange(3)
        revealed_goat = next(i for i in range(3) if i != player_choice and doors[i] == 0)
        stay_wins += doors[player_choice]
        switch_wins += doors[next(i for i in range(3) if i != player_choice and i != revealed_goat)]

    print(f"Статистика при остании при выборе: {stay_wins} выигрышей из {simulations} попыток.")
    print(f"Статистика при переключении выбора: {switch_wins} выигрышей из {simulations} попыток.")

if __name__ == "__main__":
    num_simulations = int(input("Введите количество симуляций: "))
    monty_hall_paradox(num_simulations)
