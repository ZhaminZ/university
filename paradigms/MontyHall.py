import random

def monty_hall(iterations):
    switch_wins = 0
    stay_wins = 0

    for _ in range(iterations):
        doors = [0, 0, 1]
        random.shuffle(doors)
        choice = random.randrange(3)

        opened_door = [i for i in range(3) if i != choice and doors[i] == 0][0]

        new_choice = [i for i in range(3) if i != choice and i != opened_door][0]

        if doors[new_choice] == 1:
            switch_wins += 1
        if doors[choice] == 1:
            stay_wins += 1

    switch_percentage = (switch_wins / iterations) * 100
    stay_percentage = (stay_wins / iterations) * 100

    return switch_percentage, stay_percentage
def main():
    iterations = int(input('Введите количество итераций: '))
    switch_percentage, stay_percentage = monty_hall(iterations)
    print("При изменении выбора выигрыш произошел в", switch_percentage, "% случаев")
    print("При сохранении выбора выигрыш произошел в", stay_percentage, "% случаев")


if __name__ == "__main__":
    main()
    