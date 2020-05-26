nums = 1, 2, 3, 4, 5, 6
with open('task_5.txt', 'w') as f:
    f.writelines(' '.join(map(str, nums)))
    print(sum(nums))
