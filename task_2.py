my_list = []
while True:
	inp = input('Введите элемент списка. Для прекращения ввода введите \'q\': ')
	if inp == 'q':
		break
	my_list.append(inp)
print('Ваш список:', my_list)
for i in range(1, len(my_list), 2):
	my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print('Ваш список после обмена значений:', my_list)
