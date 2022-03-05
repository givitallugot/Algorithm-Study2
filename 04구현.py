## 왕실의 나이트

# ord('a') # 97~105

rowcol = input()
col = ord(rowcol[0])
row = int(rowcol[1])

print(row, col)
# 행, 열
drdc = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
cnt = 0

for d in drdc:
    
    if (col + d[1]) >= 97 and (col + d[1]) <= 105:
        if (row + d[0]) >= 1 and (row + d[0]) <= 8:
            print(col + d[1], row + d[0], 'T')
            cnt += 1

# 겹치는 경우는 없을 것
print(cnt)

