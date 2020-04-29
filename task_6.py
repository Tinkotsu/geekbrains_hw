run = int(input('Введите результат пробежки в 1й день: '))
goal = int(input('Введите цель спортсмена: '))
i = 1
while run < goal:
    run *= 1.1
    i += 1
print(i)
