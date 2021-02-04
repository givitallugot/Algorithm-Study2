import sys
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/1. k번째 약수/in5.txt", "rt")

# K번째 약수
N, K = input().split()
N = int(N); K = int(K)

l = []
k = 1
for i in range(N):
    if (N%(i+1) == 0):
        l.append(i+1)
        if k == K:
            print(k, "번째 작은 약수: ", i+1)
            break
        elif i+1 == N:
            print('-1')
        k=k+1

print(l)