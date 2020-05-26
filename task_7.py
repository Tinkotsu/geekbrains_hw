import json

firm_dict = dict()
avg_dict = dict()
with open('task_7.txt') as f:
    i = 0
    f_sum = 0
    for line in f.readlines():
        name, firm_t, income, costs = line.split()
        profit = int(income) - int(costs)
        firm_dict.update({name: profit})
        if profit > 0:
            i += 1
            f_sum += profit
    avg_dict.update({"average_profit": f_sum / i})
with open('task_7_ans.json', 'w', encoding='utf-8') as f:
    json.dump([firm_dict, avg_dict], f, ensure_ascii=False)
