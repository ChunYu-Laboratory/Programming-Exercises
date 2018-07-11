# 1. 三角形邊長 Input

side_input = input()

# 2. 切割輸入字串分隔之空白成 list

side = side_input.split(' ')

# 3. 轉換 side 內元素成 int 型式

side = list(map(int, side))

# 4. 排序 side 內元素

side.sort()

# 5. 轉換 side 內元素成 str 型式

side_str = list(map(str, side))

# 6. 將 side_str 內的元素以空白間格合成字串

side_output = ' '.join(side_str)

# 7. 輸出排序後的邊長字串

print(side_output)

# 8. 使用畢氏定理判斷三角形類型並輸出

if side[0] + side[1] <= side[2] :
    print('No')
elif (side[0])**2 + (side[1])**2 < (side[2])**2 :
    print('Obtuse')
elif (side[0])**2 + (side[1])**2 == (side[2])**2 :
    print('Right')
elif (side[0])**2 + (side[1])**2 > (side[2])**2 :
    print('Acute')
