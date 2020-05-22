from sys import argv

if 'h' not in argv and 'help' not in argv and len(argv) != 4:
    print('Некорректный ввод. Для помощи введите \'h\' или \'help\'.')
elif 'h' in argv or 'help' in argv:
    print('Порядок аргументов: "выработка в часах" "ставка в час" "премия".')
else:
    print('Заработная плата сотрудника =',
          int(argv[1]) * int(argv[2]) + int(argv[3]))
