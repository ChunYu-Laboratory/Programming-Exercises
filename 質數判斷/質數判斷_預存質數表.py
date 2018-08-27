f = open('prime_list.json')
import json
prime_list = json.loads(f.read())

def n_input():
    while True:
        n = input('請輸入大於 1 之正整數：')
        if n.isdigit():
            n = int(n)
            if n > 1:
                break
            else:
                print('輸入格式錯誤',end='\n\n')
        else:
            print('輸入格式錯誤',end='\n\n')
    return n

def check():
    if n in prime_list:
        print(n,'is a prime number')

def factorization():
    status = True
    for x in prime_list:
        if x*x > n:
            break
        if n % x == 0:
            print(n,'not a prime number')
            status = False
            break
    if status:
        for x in range(prime_list[-1]+1, n+1):
            if x*x > n:
                break
            if n % x == 0:
                print(n,'not a prime number')
                status = False
                break
    if status:
        print(n,'is a prime number')

print('<< 質數判斷程式 >>',end='\n\n')
n = n_input()
print()
import time
start = time.clock()
if n <= 10000000:
    check()
else:
    factorization()
end = time.clock()

print()
elapsed = end - start
print('Time taken：', elapsed, 'seconds')