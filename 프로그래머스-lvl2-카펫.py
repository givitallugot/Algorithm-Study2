# 완전탐색

def solution(brown, yellow):
    answer = []
    wh = (brown - 4)//2
    for h in range(1, wh//2+1, 1):
        # wh-h: width, h: height
        if h*(wh-h) == yellow:
            answer = [wh-h+2, h+2]
            break
    return answer
