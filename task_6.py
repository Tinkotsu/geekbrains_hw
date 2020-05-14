import sys
res = []
shop_dict = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
i = 1
while True:
	new = shop_dict.copy()
	for elem in new:
		while True:
			inp = input('Заполните категорию "' + elem + '": ')
			if elem == 'цена' or elem == 'количество':
				try:
					inp = int(inp)
				except ValueError:
					print('Ошибка! Введено не число.')
					continue
			break
		new[elem] = inp
	res.append((i, new))
	inp = input('\nДля продолжения введите любой символ. Для выхода введите \'q\': ')
	if inp == 'q':
		break
	i += 1
print('\nВаша структура:', res)

for elem in res:
	for item in elem[1]:
		shop_dict.get(item).append(elem[1].get(item))
print('\nАналитика о товарах:', shop_dict)
