# 1. Input

num_input = input()

# 2. 將輸入數字字串每一位數分別放入 list 中

num = list(num_input)

# 3. 轉換 num 內元素成 int 型式

num = list(map(int, num))

# 4. 使用 loop 掃過 num list 於相鄰數字進行變號運算並加總

sign = 1
total = 0
for digit in num:
  total += sign * digit
  sign = -sign

# 5. 輸出運算後之絕對差值

print(abs(total))