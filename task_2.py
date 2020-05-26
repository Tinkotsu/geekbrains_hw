with open('task_2.txt') as f:
    i = 0
    for line in f.readlines():
        i += 1
        print(f'Слов в строке номер {i}: {len(line.split())}')
    print(f'Всего строк: {i}')
