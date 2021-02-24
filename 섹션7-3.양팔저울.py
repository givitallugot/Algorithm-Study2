import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/3. 양팔저울/in1.txt')

def DFS(L, res):
    global S, Sl

    if L == N:
        if 0 < res <= S:
            Sl[res-1] = 0
        return
    else:
        DFS(L+1, res+weight[L])
        DFS(L+1, res-weight[L])
        DFS(L+1, res)



if __name__ == '__main__':
    N = int(input())
    weight = list(map(int, input().split()))

    S = sum(weight)
    Sl = [1]*S

    DFS(0, 0)
    print(sum(Sl))

# sort는 안해도 되는 것인가?