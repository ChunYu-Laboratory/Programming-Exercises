print('<< 質數判斷程式 >>','\n')
n = int(input('請輸入整數：'))
print()
factor = []
import math
for x in range(2, math.ceil(n**0.5)+1):
    if n % x == 0:
        factor.append([x,n//x])
if factor == []:
    print(n, 'is a prime number')
else:
    print(n,'with the following factors','\n')
    print(factor)
print()
print('-----Finished-----')

