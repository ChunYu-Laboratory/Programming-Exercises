factor = []
for x in range(1, n+1):
    if x*x > n:
        break
    if n % x == 0:
        factor.append([x,n//x])
if factor == [[1,n]]:
    print(n, 'is a prime number')
else:
    print(n,'with the following positive factors：',end='\n\n')
    print(factor)