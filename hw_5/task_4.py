with open('task_4.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if '1' in lines[i]:
            lines[i] = lines[i].replace('One', 'Один')
        elif '2' in lines[i]:
            lines[i] = lines[i].replace('Two', 'Два')
        elif '3' in lines[i]:
            lines[i] = lines[i].replace('Three', 'Три')
        elif '4' in lines[i]:
            lines[i] = lines[i].replace('Four', 'Четыре')

with open('new_task_4.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
