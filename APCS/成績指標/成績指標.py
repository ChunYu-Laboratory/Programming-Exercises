# 1. Input

num = input()
score_input = input()

# 2. 切割輸入成績字串分隔之空白成 list

score = score_input.split(' ')

# 3. 轉換 score 內元素成 int 型式

score = list(map(int, score))

# 4. 排序 score 內元素

score.sort()

# 5. 轉換 score 內元素成 str 型式

score_str = list(map(str, score))

# 6. 將 score_str 內的元素以空白間格合成字串

score_output = ' '.join(score_str)

# 7. 輸出排序後的成績字串

print(score_output)

# 8. 新增空 list 存放 及格 與 不及格 分數

f = []
p = []

# 9. 從 score list 中提取元素、判斷分數並存入相應之 list 中

for x in score :
    if x < 60 :
        f.append(x)
    else :
        p.append(x)

# 10. 排序分數 list 以便後續存取第一個元素

f.reverse()
p.sort()

# 11. 判斷條件並輸出

if f == [] :
    print('best case')
else :
    print(f[0])
if p == [] :
    print('worst case')
else :
    print(p[0])
