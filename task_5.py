n_sum = 0
running = 1
print('Для выхода введите \'q\' вместо числа \n')
while running:
    inp = input('Введите числа через пробел: ').split()
    if 'q' in inp:
        inp.remove('q')
        running = 0
    n_sum += sum(map(int, inp))
    print('Текущая сумма =', n_sum, '\n')
