prime_list = []
for n in range(2,10000000):
    status = True
    for x in range(2,n+1):
        if x*x > n:
            break
        if n % x == 0:
            status = False
            break
    if status:
        prime_list.append(n)

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