def range_input():
    while True:
        try:
            r1 = int(input('請輸入整數範圍起始值：'))
            break
        except ValueError:
            print('輸入格式錯誤',end='\n\n')
    while True:
        while True:
            try:
                r2 = int(input('請輸入整數範圍中止值：'))
                break
            except ValueError:
                print('輸入格式錯誤',end='\n\n')
        if r2 >= r1:
            break
        else:
            print('中止值必須大於或等於起始值',end='\n\n')
    return r1,r2
def int_input():
    while True:
        while True:
            try:
                if count == 0:
                    i = int(input('請猜出電腦隨機產生之範圍內整數：'))
                    break
                else:
                    i = int(input('請再次輸入：'))
                    break
            except ValueError:
                print('輸入格式錯誤',end='\n\n')
        if r1 <= i <= r2:
            break
        else:
            print('數字必須介於範圍之間',end='\n\n')
    return i
print('<< 猜數字遊戲 >>',end='\n\n')
r1,r2 = range_input()
from random import randint
x = randint(r1,r2)
print(end='\n\n')
count = 0
i = int_input()
count = 1
while i != x:
    print('作答次數：',count,sep='')
    if i > x:
        print('太大了',end='\n\n')
        i = int_input()
    elif i < x:
        print('太小了',end='\n\n')
        i = int_input()
    count += 1
print('作答次數：',count,sep='')
print('答對了')