my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]])  # 1 часть

print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])  # 2 часть