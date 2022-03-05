## 큰 수의 법칙
n, m, k = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)

tot = 0

tot += (l[0] * (m // (k+1)) * k) + (l[0] * (m % (k+1)))
tot += l[1] * (m // (k+1))

print(tot)

## 숫자 카드 게임
n, m = map(int, input().split())

max = 0
for i in range(n):
   l = list(map(int, input().split()))
   if max < min(l):
       max = min(l)

print(max)