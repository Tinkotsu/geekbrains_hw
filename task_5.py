from itertools import cycle, count

for i in count(int(input('Введите начало отсчета: '))):  # решение первой части задания
    if i > 100:  # останавливаю цикл, если досчитали до 100
        break
    print(i)


my_list = input('Введите элементы списка через пробел: ').split()  # решение второй части задания
for elem in cycle(my_list):
    print(elem)
    if my_list.index(elem) == len(my_list) - 1:
        if input('Для продолжения введите любой символ. Для выхода введите \'q\': ') == 'q':
            break

