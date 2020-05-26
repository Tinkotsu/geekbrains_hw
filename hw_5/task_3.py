with open('task_3.txt') as f:
    i = 0
    sal = 0
    for line in f.readlines():
        i += 1
        name, amount = line.split()
        amount = float(amount)
        sal += amount
        if amount < 20000:
            print(name)
    print(f'Средняя величина дохода: {sal / i}')
