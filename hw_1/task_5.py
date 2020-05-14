earns = int(input('Введите значение выручки: '))
losses = int(input('Введите значение издержек: '))
profit = earns - losses
if profit > 0:
    print('Фирма получает прибыль')
    print(f'Рентабельность выручки = {(profit / earns):.2f}')
    workers_num = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на одного сотрудника = {(profit / workers_num):.2f}')
elif profit < 0:
    print('Фирма несет убытки')
else:
    print('Фирма работает в ноль')


