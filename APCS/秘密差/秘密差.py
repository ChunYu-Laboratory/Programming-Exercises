# 1. Input

num_input = input()

# 2. 將輸入數字字串每一位數分別放入 list 中

num = list(num_input)

# 3. 轉換 num 內元素成 int 型式

num = list(map(int, num))

# 4. 數字位數之奇偶判斷並分別將奇數位數放入 a 偶數位數放入 b

if len(num) % 2 == 0 :
    a = num[1::2]
    b = num[::2]
else :
    a = num[::2]
    b = num[1::2]

# 5. 計算奇數位數和 A 與 偶數位數和 B

A = sum(a)
B = sum(b)

# 6. 輸出兩數之絕對差值

print(abs(A-B))
