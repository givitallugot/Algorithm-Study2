
#  NXN 행렬의 (i,j)를 (j,i) => 한 줄로 바꾸는 방법

## 방법 1
list(map(list, zip(*scores)))

## 방법 2
score=[ [i[j] for i in scores] for j in range(len(scores))]



import numpy as np

def solution(scores):
    answer = ''
    N = len(scores)
    M = []

    for i in range(N):
        score = []
        for j in range(N):
            score.append(scores[j][i])

        my = scores[i][i]
        score.sort(reverse=True)
        if (my == score[0]) & (score[0] != score[1]):
            score.remove(my)
        elif (my == score[N-1]) & (score[N-1] != score[N-2]):
            score.remove(my)

        M.append(np.mean(score))

    for m in M:
        if m >= 90:
            answer = answer + 'A'
        elif 80 <= m < 90:
            answer = answer + 'B'
        elif 70 <= m < 80:
            answer = answer + 'C'
        elif 50 <= m < 70:
            answer = answer + 'D'
        else:
            answer = answer + 'F'

    return answer

