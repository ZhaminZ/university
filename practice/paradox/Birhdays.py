import random

def birthday_paradox(iterations):
    matching_birthdays_count = 0

    for _ in range(iterations):
        birthdays = [random.randint(1, 365) for _ in range(23)]
        if len(birthdays) != len(set(birthdays)):
            matching_birthdays_count += 1

    probability = matching_birthdays_count / iterations * 100
    return probability

if __name__ == "__main__":
    num_simulations = int(input("Введите количество симуляций: "))
    print("Вероятность совпадения дней рождения:", birthday_paradox(num_simulations))
