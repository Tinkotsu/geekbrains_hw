my_dict = dict()
with open('task_6.txt') as f:
    for line in f.readlines():
        name = ''
        num = 0
        for word in line.split():
            if ':' in word:
                name = word.split(':')[0]
            if '(' in word:
                num += int(word.split('(')[0])
        my_dict.update({name: num})
print(my_dict)
