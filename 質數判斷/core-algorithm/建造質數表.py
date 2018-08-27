f = open('prime_list.json',mode='w')

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

import json
j = json.dumps(prime_list)
f.write(j)