import random


def take_order():
    print('—--Кафе “У Монті”---')
    print('---Введіть список страв---')
    input_data = input()
    return input_data


def print_order(list):
    summa = 0
    for i in list:
        rnd = random.randint(1, 100)
        summa += rnd
        print(str(i) + '........' + str(rnd) + 'грн.')
    print('...................................')
    print('Всього........' + str(summa))


list_data = take_order().split(',')

print_order(list_data)
