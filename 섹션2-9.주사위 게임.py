import sys
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/9. 주사위 게임/in5.txt", "rt")

N = int(input())

# true 1, false 0 이용
def check_price(p):
    condi = [p[0] == p[1], p[1] == p[2], p[0] == p[2]]

    if sum(condi) == 3:
        price = 10000+p[0]*1000
    elif sum(condi) == 1:
        tn = condi[0]*1 + condi[1]*2 + condi[2]*3 # To check one of true number, 1이면 첫번째두번째, 2이면 두번째세번째, 3이면 첫번째세번째 같은 숫자
        price = 1000+p[tn-1]*100
    else:
        price = max(p)*100

    return price

price_list = []

for i in range(N):
    p = list(map(int, input().split()))
    price_list.append(check_price(p))

print(max(price_list))

# 매우 잘짠 코드라고 생각