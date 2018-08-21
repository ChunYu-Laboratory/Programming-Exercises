from random import randint
print('<< 猜數字遊戲 >>',end='\n\n')
r1 = int(input('請輸入整數範圍起始值：'))
r2 = int(input('請輸入整數範圍中止值：'))
x = randint(r1,r2)
i = int(input('請猜出電腦隨機產生之範圍內整數：'))
count = 1
while i != x:
    print('作答次數：',count,sep='')
    if i > x:
        print('太大了',end='\n\n')
        i = int(input('請再次輸入：'))
    elif i < x:
        print('太小了',end='\n\n')
        i = int(input('請再次輸入：'))
    count += 1
print('作答次數：',count,sep='')
print('答對了')
