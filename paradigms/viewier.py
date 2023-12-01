from Paradigms.Birthdays import *
from Paradigms.MontyHall import *


def show():
    while True:
        print("\nВыберите парадокс: ")
        print("1.Монти Холла")
        print("2. День Рождения")
        choise = input()

        if choise==1:
            print('1. "Монти Холла":')
            x = int(input('Введите кол-во итераций: '))
            print(monty_hall(x))
        elif choise==2:
            print('2. "День рождения":')
            people = int(input('Введите кол-во человек в группе: '))
            repeats = int(input('Введите кол-во итераций: '))
            print(birth(people,repeats))   
        else:
            break                              


if __name__ == "__main__":
    show()