# 동적계획법 문제, N으로 표현보다는 조금 더 쉬운 난이도

def solution(triangle):
    answer = 0
    N = len(triangle[-1])
    table = [[-1]*N for _ in range(N)]

    table[0][0] = triangle[0][0]
    for i in range(1,N):
        for j in range(i+1):        
            if (j-1) < 0: # 왼쪽 끝인 경우
                table[i][j] = table[i-1][j] + triangle[i][j]
            elif table[i-1][j] == -1: # 오른쪽 끝인 경우
                table[i][j] = table[i-1][j-1] + triangle[i][j]
            else: # 그 외의 경우 바로 윗줄(i-1) 같은 위치(j)와 윗줄(i-1) 하나 앞의 위치(j-1) 중 큰 값
                table[i][j] = max(table[i-1][j-1], table[i-1][j]) + triangle[i][j]

    answer = max(table[-1])
    return answer