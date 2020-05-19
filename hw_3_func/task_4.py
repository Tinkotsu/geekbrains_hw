def my_func(x, y):
    return x ** y


def my_func_cycle(x, y):
    res = 1
    for _ in range(abs(y)):
        res /= x
    return res


n1 = float(input('Введите положительное число x: '))
n2 = int(input('Введите целое отрицательное число y: '))
if n1 <= 0 or n2 >= 0:
    print('Ошибка! Некорректный ввод.')
else:
    print('Решение с "**":', my_func(n1, n2))
    print('Решение через цикл:', my_func_cycle(n1, n2))
