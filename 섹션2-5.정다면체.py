import sys
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/5. 정다면체/in5.txt", "rt")

N, M = map(int, input().split())
Nshape = list(range(1,N+1))
Mshape = list(range(1,M+1))
All = dict()

for i in range(N):
    for j in range(M):
        sm = Nshape[i] + Mshape[j]
        if sm in All.keys():
            All[sm] = All[sm] + 1
        else:
            All[sm] = 1
        # All.append()

All = sorted(All.items(), reverse=True, key=lambda item: item[1]) 
# 자동으로 key는 오름차순 sort 됨

Yes = [All[i][0] for i in range(len(All)) if All[i][1] == All[0][1]]
print(*Yes, sep=' ')