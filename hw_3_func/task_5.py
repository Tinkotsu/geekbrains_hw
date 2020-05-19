n_sum = 0
running = 1
print('Для выхода введите \'q\' вместо числа \n')
while running:
    inp = input('Введите числа через пробел: ').split()
    for elem in inp:
        if elem == 'q':
            running = 0
            break
        try:
            n_sum += int(elem)
        except ValueError:
            print(f'Элемент "{elem}" проигнорирован - некорректный ввод.')
    print('Текущая сумма =', n_sum, '\n')
