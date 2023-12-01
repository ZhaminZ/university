import random

def birth(people, repeats):
    answer = 0

    for _ in range(repeats):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            answer += 1

    percentage = (answer / repeats) * 100

    return f"Количество групп с как минимум двумя людьми с одинаковыми днями рождения: {answer}, Процент таких групп от общего числа итераций: {percentage}%"
def main():
    people = int(input("Введите количество людей в группе: "))
    repeats = int(input("Введите количество итераций: "))

    result = birth(people, repeats)
    print(result)
if __name__ == "__main__":
    main()