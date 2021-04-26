
def solution(board, moves):
    answer = 0
    N = len(board)
    top = [0]*N # 쌓여있는 개수
    result = [0] # 0번 인형은 없으므로 초기값으로 설정

    for i in range(N):
        for j in range(N):
            if (board[i][j] > 0) & (top[j] < N-i):
                # 현재 인형이 쌓여있는 위치, 지금 기록된 위치보다 높을 때 (즉 0이 아닐 때)
                top[j] = N-i

    for m in moves:
        mlast = top[m-1]
        if mlast == 0:
            continue
        else:
            new = board[N-mlast][m-1] # 가장 위에 있는 위치 인형
            board[N-mlast][m-1] = 0 # 인형 뽑기
            top[m-1] -= 1 # 쌓여있는 개수 내리기

            # 같은 인형이라면
            if new == result[-1]:
                result.pop()
                answer += 2

            # 같은 인형 아니라면
            else:
                result.append(new)

    return answer
