def solution(weights, head2head):
    answer = []
    summary = []
    number = len(weights)
    # 번호, 자기 몸무게, 자기보다 무거운 복서 이긴 횟수, 승률
    
    for i, w in enumerate(weights):
        res = head2head[i]; total = 0; wl = 0; mw = 0
        for j in range(number):
            if res[j] == 'W':
                total += 1
                wl += 1
                if weights[j] > weights[i]:
                    mw += 1
            elif res[j] == 'L':
                total += 1
        
        if total == 0 or wl == 0:
            summary.append([i+1, weights[i], mw, 0])
        else:
            summary.append([i+1, weights[i], mw, 100*wl/total ,2])
            
    summary.sort(key=lambda x: x[0])
    summary.sort(key=lambda x: x[1], reverse = True)
    summary.sort(key=lambda x: x[2], reverse = True)
    summary.sort(key=lambda x: x[3], reverse = True)
    # summary.sort(key=lambda x: (x[3], x[2], x[1], -x[0]), reverse = True)
    # 또는 번호를 음수로 넣었다면 그냥 한번에 summary.sort(reverse = True)로 해결 가능

    answer = [x[0] for x in summary]
    
    return answer