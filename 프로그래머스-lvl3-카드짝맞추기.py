# BFS 로 푸는 문제, 53점
# 미완성.. 코드..

# 이 Ctrl Move를 제대로 구현하면 점수가 올라갈 듯 보임
### [Ctrl] 키를 누른 상태에서 방향키 ←, ↑, ↓, → 중 하나를 누르면, 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동합니다.
### 만약, 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동합니다.

def findmatch(board, card, r, c):
    for row in range(4):
        for col in range(4):
            if (row == r) and (col == c):
                continue
            if board[row][col] == card:
                return [row,col]

def solution(board, r, c):
    answer = 0
    cards = []
    
    # 먼저 현재 0이 아닌 위치 다 찾기
    for row in range(4):
        for col in range(4):
            if board[row][col] != 0:
                cards.append([row,col])
    
    # 만약 r,c 가 cards에 있을 때 없을 때 나눠서
    # 없을 때 현재 위치에서 가장 가까운 곳으로
    while cards:
        if [r,c] in cards:
            answer += 1
            card = board[r][c]
            nr, nc = findmatch(board, card, r, c)
            if (nr != r) and (nc != c):
                answer += 2
            else:
                answer += 1

            cards.remove([r,c])
            cards.remove([nr,nc])
            answer += 1 # enter
            r = nr; c = nc
        else:
            dist = 0
            for [nnr,nnc] in cards: # 더 가까운 위치를 찾기 위해서,
                if (r == nnr) or (c == nnc): # row, col 둘 중 하나만 움직임
                    r = nnr; c = nnc
                    answer += 1
                    break
                else: # row, col 둘 다 움직임
                    r = nnr; c = nnc
                    continue
            else:
                answer += 2 

    # 다음 최솟값. 가까운 거리
    return answer



#### 참고용 코드 (블로그 참고, https://cocook.tistory.com/117)
# 방향키로만 움직일 때
def withoutCtrl(board,row,col):
    result =[]
    for drow, dcol in moves:
        nrow = row + drow
        ncol =col +dcol
        if 0<= nrow < 4 and 0<= ncol < 4:
            result.append((nrow, ncol,))
            
    return result

#컨트롤을 이용해 움직일 때
def withCtrl(board,r, c):
    result =[]
    for drow, dcol in moves:
        row=r
        col=c
        while True:
            row += drow
            col += dcol
            if row < 0 or row >= 4 or col < 0 or col >= 4:
                if not(row-drow == r and col-dcol == c):
                    result.append([row-drow, col-dcol])
                break
                
            if board[row][col] != 0:
                result.append([row, col])
                break
                
    return result