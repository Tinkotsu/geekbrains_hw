def int_func(text):
    res = text[0].upper() + text[1:]
    return res


print(int_func('text'))

print(' '.join(list(map(int_func, input('Введите строку: ').split()))))
