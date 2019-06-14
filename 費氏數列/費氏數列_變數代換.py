def fibo(n):
    table = [0]*3
    table[0], table[1] = 0, 1
    for i in range(1,n):
        table[2] = table[1] + table[0]
        table[0], table[1] = table[1], table[2]
    return table[2]

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
A = fibo(n)
end = time.clock()

print('Answer：', A)

print()
print('The length of digit：', len(str(A)))

print()
elapsed = end - start
print('Time taken：', elapsed, 'seconds')