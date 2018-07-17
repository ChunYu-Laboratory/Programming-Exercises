# 1. R,C,M Input

RCM_input = input()

# 2. 切割輸入字串分隔之空白成 list

RCM = RCM_input.split(' ')

# 3. 轉換 RCM 內元素成 int 型式

RCM = list(map(int, RCM))

# 4. 宣告 R,C 變數

R = RCM[0]
C = RCM[1]

# 5. 宣告空 list 並將輸入的 R 行值處理變成 list 加入-----以 2 維 list 模擬矩陣

B = []
for i in range(R) :
    temp_input = input()
    temp = temp_input.split(' ')
    temp = list(map(int, temp))
    B.append(temp)

# 6. 矩陣操作參數輸入及處理

M_input = input()
M = M_input.split(' ')
M = list(map(int, M))

# 7. 因是從操作後的矩陣回推原矩陣，所以需反向操作-----將操作參數反轉

M = M[::-1]

# 8-1. 定義「翻轉」函數

def flip(mx) :
    mx = mx[::-1]
    return mx

# 8-2. 定義「旋轉」函數 (逆時針旋轉 90 度 以回推原矩陣)-----先建立與輸入矩陣行列數互換之 0 矩陣 再進行元素代換

def rotate(mx, r, c) :
    x = [[0 for i in range(r)] for j in range(c)]
    for i in range(r) :
        for j in range(c) :
            x[c-j-1][i] = mx[i][j]
    return x

# 9. 操作參數判斷並使用函數進行操作

for z in M :
    if z == 0 :
        B = rotate(B, len(B), len(B[0]))
    elif z == 1 :
        B = flip(B)

# 10. 原矩陣之列數及行數以 string format 方式以空白分隔並輸出

RC_output = '{R} {C}'.format(R=len(B), C=len(B[0]))
print(RC_output)

# 11. 以原矩陣的列數輸出矩陣，每行輸出元素皆以空白分隔

for i in B :
    temp_C_str = list(map(str, i))
    C_output = ' '.join(temp_C_str)
    print(C_output)
