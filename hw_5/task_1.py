print('Ввод текст в файл. Для остановки введите пустую строку.')
with open('task1.txt', 'w') as f:
    while True:
        to_write = input()
        if not to_write:
            break
        f.write(to_write + '\n')
