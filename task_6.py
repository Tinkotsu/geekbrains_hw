def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res
    else:  # сделал проверку на 0!, хоть и в задании не выводим этот случай
        yield 1


num = int(input('Введите положительное число: '))
if num <= 0:
    print('Некорректный ввод.')
    exit()
k = 1
for el in fact(num):
    print(f'{k}! = {el}')
    k += 1
