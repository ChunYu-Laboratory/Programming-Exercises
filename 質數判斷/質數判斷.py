print('<< 質數判斷程式 >>','\n')
n = int(input('請輸入大於 1 之正整數：'))
print()
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
print()
print('-----Finished-----')