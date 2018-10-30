def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

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