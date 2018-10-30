with open('fibo_list.json') as file:
    import json
    fibo_list = json.loads(file.read())

def check(n):
    return(fibo_list[n])

def compute(n):
    table = [0]*3
    table[0], table[1] = fibo_list[-2], fibo_list[-1]
    for i in range(0,n-100000):
        table[2] = table[1] + table[0]
        table[0], table[1] = table[1], table[2]
    return(table[2])

def n_input():
    while True:
        n = input('請輸入項數：')
        if n.isdigit():
            n = int(n)
            if n >= 0:
                break
            else:
                print('輸入格式錯誤 | 項數需為大於或等於 0 之整數',end='\n\n')
        else:
            print('輸入格式錯誤 | 項數需為大於或等於 0 之整數',end='\n\n')
    return n

print('<< 費氏數列第 n 項計算程式 >>',end='\n\n')
n = n_input()
print()

import time
start = time.clock()
if n>100000:
    fibo = compute(n)
else:
    fibo = check(n)
end = time.clock()

print('Answer：', fibo)

print()
print('The length of digit：', len(str(fibo)))

print()
elapsed = end - start
print('Time taken：', elapsed, 'seconds')