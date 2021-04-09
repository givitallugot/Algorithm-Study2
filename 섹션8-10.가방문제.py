import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/10. 동전교환/in2.txt')

# 동전 c = 1, 2, 5, dy는 500으로 초기화
# dy[i] = min(dy[i], dy[i-c] + 1) 거슬러줄 금액이 i일 때, 지금까지 동전 최소 개수값
# dy[c] = 1부터 시작

if __name__ == '__main__':
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dy=[500]*(M+1)
    for c in coin:
        dy[c] = 1
        for j in range(c, M+1):
            dy[j] = min(dy[j], dy[j-c] + 1)

    print(dy)
    
    print(dy[M])
