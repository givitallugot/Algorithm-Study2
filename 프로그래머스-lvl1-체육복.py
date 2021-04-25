# https://programmers.co.kr/learn/courses/30/lessons/42862
# 탐욕법

# point1: reverse에 대한 정렬이 필요 ex [3, 5], [4, 2], 원래 둘 다 커버 되는데 정렬이 안되었다면 순서대로 찾을 때 문제
# point2: 여벌이 있더라도 본인 체육복 도난당했다면 빌려줄 수 없음, 미리 처리해야 됨 (뒤에 for를 돌면서 처리하면 다른사람에게 주고 본인이 못입게 될 수도) ex [3, 4], [4, 2]

def solution(n, lost, reserve):
    answer = 0
    students = [1]*(n+2) # 앞 뒤로 하나씩 추가

    lost.sort()
    reserve.sort()

    for l in lost: # 체육복 없는 친구
        # 만약 여벌 있지만 본인 체육복 도난당했다면, 빌려줄 수 없음
        if l in reserve:
            reserve.remove(l)
        else:
            students[l] = 0

    for r in reserve:
        # 체육복을 빌려줄 수 있는 경우
        if students[r-1] == 0:
            students[r-1] = 1
        elif students[r+1] == 0:
            students[r+1] = 1

#     print(students)

    answer = sum(students[1:n+1])
    return answer
