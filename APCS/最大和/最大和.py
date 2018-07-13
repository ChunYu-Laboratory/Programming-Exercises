# 1. N,M Input

NM_input = input()

# 2. 切割輸入字串分隔之空白成 list

NM = NM_input.split(' ')

# 3. 轉換 NM 內元素成 int 型式

NM = list(map(int, NM))

# 4. 宣告 N,M 變數

N = NM[0]
M = NM[1]

# 5. 宣告空 list 並將輸入的 N 行值處理變成 list 加入-----以 2 維 list 分隔各群數字

cluster = []
for i in range(N) :
    temp_input = input()
    temp = temp_input.split(' ')
    temp = list(map(int, temp))
    cluster.append(temp)

# 6. 宣告空 list 並將各群最大的數加入 list 中

max_num = []
for i in range(N) :
    temp = cluster[i]
    temp.sort(reverse = True)
    max_num.append(temp[0])

# 7. 計算各群最大數之和並輸出

S = 0
for i in max_num :
    S += i
print(S)

# 8. 宣告空 list 並將可以整除 S 的被選擇數字加入 list 中

select_num = []
for i in max_num :
    if S % i == 0 :
        select_num.append(i)

# 9. 條件判斷並輸出相應值

if select_num == [] :
    print(-1)
else :
    select_num = list(map(str, select_num))
    select_num_output = ' '.join(select_num)
    print(select_num_output)
