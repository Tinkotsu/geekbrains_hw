def my_div(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print('Ошибка! Деление на ноль.')


num1, num2 = map(int, input('Введите два числа через пробел: ').split())
answer = my_div(num1, num2)
if answer:
    print('Ответ:', answer)
