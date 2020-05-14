time = int(input('Введите время в секундах: '))
hours = time // 3600
time %= 3600
minutes = time // 60
sec = time % 60
print(f'{hours:02}:{minutes:02}:{sec:02}')
