with open('fibo_list.json', mode='w') as file:
    fibo_list = [0, 1]
    table = [0]*3
    table[0], table[1] = 0, 1
    for i in range(1,100000):
        table[2] = table[1] + table[0]
        fibo_list.append(table[2])
        table[0], table[1] = table[1], table[2]
    import json
    file.write(json.dumps(fibo_list))