factor = [[1,n]]
import math
for x in range(2, math.ceil(n**0.5)+1):
    if n % x == 0:
        factor.append([x,n//x])
if factor == [[1,n]]:
    print(n, 'is a prime number')
else:
    print(n,'with the following positive factors','\n')
    print(factor)