with open('prime_list.json',mode='w') as file:
    prime_list = []
    for n in range(2,100000000):
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
    file.write(json.dumps(prime_list))