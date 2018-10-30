def check(n):
    return(fibo_list[n])

def compute(n):
    table = [0]*3
    table[0], table[1] = fibo_list[-2], fibo_list[-1]
    for i in range(0,n-100000):
        table[2] = table[1] + table[0]
        table[0], table[1] = table[1], table[2]
    return(table[2])

if n>100000:
    fibo = compute(n)
else:
    fibo = check(n)