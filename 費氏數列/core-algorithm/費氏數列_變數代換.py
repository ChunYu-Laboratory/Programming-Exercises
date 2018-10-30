def fibo(n):
    table = [0]*3
    table[0], table[1] = 0, 1
    for i in range(1,n):
        table[2] = table[1] + table[0]
        table[0], table[1] = table[1], table[2]
    return table[2]