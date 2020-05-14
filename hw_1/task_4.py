num = int(input('Введите число: '))
max_dig = 0
while num > 0:
    if num % 10 > max_dig:
        max_dig = num % 10
    num //= 10
print(max_dig)
