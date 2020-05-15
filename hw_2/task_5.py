my_list = [7, 5, 3, 3, 2]
while True:
	inp = input('Введите элемент списка. Для прекращения ввода введите \'q\': ')
	if inp == 'q':
		break
	try:
		inp = int(inp)
	except ValueError:
		print('Ошибка. Введено не число.')
		continue
	if inp <= my_list[-1]:
		my_list.append(inp)
	else:
		for i in range(len(my_list)):
			if inp > my_list[i]:
				my_list.insert(i, inp)
				break
	print(my_list)
