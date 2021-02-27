import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/5. 동전분배하기/in5.txt')

def DFS(L, Pl):
    global D
    
    if L == N:
        if (max(Pl) - min(Pl)) < D:
            if len(set(Pl)) == 3:
                D = max(Pl) - min(Pl)
                print(Pl)
        return
    else:
        Pl[0] += cv[L]
        DFS(L+1, Pl)
        Pl[0] -= cv[L]

        Pl[1] += cv[L]
        DFS(L+1, Pl)
        Pl[1] -= cv[L]

        Pl[2] += cv[L]
        DFS(L+1, Pl)
        Pl[2] -= cv[L]

if __name__ == "__main__":
    N = int(input())
    cv = list()
    D = 2147000000

    for _ in range(N):
        cv.append(int(input()))

    DFS(0, [0, 0, 0])
    print(D)

# O X 문제와 비슷, 1, 2, 3 중 하나
# [0, 0, 0]: 각 사람에게 준 돈 합