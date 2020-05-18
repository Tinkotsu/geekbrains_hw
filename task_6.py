def int_func(text):
    res = text[0].upper() + text[1:]
    return res


print(int_func('text'))

res_str = ''
for word in map(int_func, input('Введите строку: ').split()):
    res_str += word + ' '
print(res_str.rstrip())
