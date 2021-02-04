import sys
import time
starttime = time.time()

sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/10. 스도쿠 검사/in5.txt')
sudoku = []
check = [[], [], [], [], []]
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

print()

for i in range(9):
    if len(set(sudoku[i])) != 9: # i행 확인
        print('NO')
        break
    elif len(set([s[0] for s in sudoku])) != 9: # i열 확인
        print('NO')
        break
    elif i < 3: # 네모 상자 확인을 위한 계산 (여기 틀림)
        for j in range(3):
            check[0].append(sudoku[i][j])
            check[1].append(sudoku[i][j+3])
            check[2].append(sudoku[i][j+6])
            check[3].append(sudoku[i+3][j])
            check[4].append(sudoku[i+3][j+3])
            check[5].append(sudoku[i+3][j+6])
            check[6].append(sudoku[i+6][j])
            check[7].append(sudoku[i+6][j+3])
            check[8].append(sudoku[i+6][j+6])
else:
    for k in range(9): # 네모 상자 확인
        if len(set(check[k])) != 9: # i행 확인
            print('NO')
            break
    else:
        print('YES')

endtime = time.time()
print('걸린 시간: ', endtime - starttime)




# for i in range(3):
#     for j in range(3):
#         check[0].append(sudoku[i][j])
#         check[1].append(sudoku[i][j+6])
#         check[2].append(sudoku[i+3][j+3])
#         check[3].append(sudoku[i+6][j])
#         check[4].append(sudoku[i+6][j+6])
# print(check)

