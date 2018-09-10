# 1. N Input

N = int(input())

# 2. 依序輸入相應 Index 的 好友編號，並切割輸入字串分隔之空白成 list，及轉換 list 中元素之型別從 str 至 int

friend = list(map(int,input().split(' ')))

# 3. 建立 list 用以標記迴圈追蹤過的好友編號

track = [False for i in range(N)]

# 4. 宣告 count 變數 紀錄小群體個數

count = 0

# 5. 使用 for 迴圈掃描尚未追蹤過的人，及向下追蹤其好友直到回歸其本身，並加以標記追蹤過的人，循環一次時增加 count 變數

for i in range(N):
    status = False
    while not track[i]:
        track[i] = True
        i = friend[i]
        status = True
    if status:
        count += 1

# 6. 顯示小群體個數

print(count)