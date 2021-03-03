import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/7. 송아지 찾기/in1.txt')

# DFS로 풀면 에러
# Level 탐색해야함, BFS, 큐로 구현

def DFS(L, V):
    global E
    global mn
    if (V < 1) or (V > 10000) or (L > mn):
        return
    if V == E:
        if mn > L:
            mn = L
        return
    else:
        DFS(L+1, V+1)
        DFS(L+1, V-1)
        DFS(L+1, V+5)

if __name__ == "__main__":
    S, E = map(int, input().split())
    mn = 214000000
    DFS(0, S)
    print(mn)


######### BFS 구현 ##########

from collections import deque
import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/7. 송아지 찾기/in5.txt')

MAX = 10000
ch = [0] * (MAX + 1) # check list
dis = [0] * (MAX + 1) # level = distance

n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0

dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5): # 세 가닥으로 뻗어나감
        if 0 < next < MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])