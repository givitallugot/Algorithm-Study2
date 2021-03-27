# Top-Down 방식, DFS()를 이용: Nm를 1m나 2m로 자르는 수를 return 받는 함수로 구현

# 맨 마지막이 1m로 잘리는 경우의 수 = (N-1)m를 1m 또는 2m로 자르는 경우의 수 + 1(남은 1m를 1m 또는 2m로 자르는 경우의 수)
# 맨 마지막이 2m로 잘리는 경우의 수 = (N-2)m를 1m 또는 2m로 자르는 경우의 수, 즉 + 2(남은 2m를 1m 또는 2m로 자르는 경우의 수)

import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/1, 2. 네트워크 선 자르기/in1.txt')

# dy라는 테이블 마찬가지로 구현 - 이미 몇 개를 만들 수 있는지 구한 길이m 에 대해서는 다시 구할 필요 없게 만들기 위해
# 메모이제이션, dy를 구해서 이미 알고 있는 값은 바로 대입해서 일종의 cut edge를 하는 것

def DFS(len):
    if dy[len] > 0: # cut edge, 즉 메모이제이션 (이게 바로 다이나믹, 이를 사용하지 않으면 그냥 재귀)
        return dy[len]
    if len == 1 or len == 2:
        return len # 1m일 때 네트워크선 자르는 방법은 1개이고, 2m일 때 네트워크선 자르는 방법은 2개
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]



if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))