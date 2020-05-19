def fact(n):
    res = 1
    if n == 0:  # сделал проверку на 0!, хоть и вывод с 1!
        yield 1
    else:
        for i in range(1, n + 1):
            res *= i
            yield res


num = int(input('Введите положительное число: '))
if num <= 0:
    print('Некорректный ввод.')
    exit()
k = 1
for el in fact(num):
    print(f'{k}! = {el}')
    k += 1
