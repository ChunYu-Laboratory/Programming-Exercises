# 1. abc Input

abc_input = input()

# 2. 切割輸入字串分隔之空白成 list

abc = abc_input.split(' ')

# 3. 轉換 abc 內元素成 int 型式

abc = list(map(int, abc))

# 4. 宣告 a、b、c 變數並轉換 a、b 之值用以進行 Bitwise Operation

if abc[0] > 0 :
    a = 1
else :
    a = 0
if abc[1] > 0 :
    b = 1
else :
    b = 0
c = abc[2]

# 5. 新增 Flag 並進行 Bitwise Operation 及條件判斷

impossible = True
if (a&b) == c :
    print('AND')
    impossible = False
if (a|b) == c :
    print('OR')
    impossible = False
if (a^b) == c :
    print('XOR')
    impossible = False
if impossible :
    print('IMPOSSIBLE')
