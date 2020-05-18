def int_func(text):
    res = text[0].upper() + text[1:]
    return res


print(int_func('text'))

for word in map(int_func, input('Введите строку: ').split()):
    print(word, end=' ')
