def my_func(v1, v2, v3):
    if v1 > v2:
        return v1 + max(v2, v3)
    else:
        return v2 + max(v1, v3)


n1, n2, n3 = map(int, input('Введите 3 аргумента: ').split())
print('Ответ:', my_func(n1, n2, n3))
