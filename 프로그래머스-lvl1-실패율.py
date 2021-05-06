def solution(N, stages):
    answer = []
    stages.sort()
    failure = dict()
    for j in range(1, N+1):
        failure[j] = 0
    
    prev = 0; cumn = 0; lb = 0
    sl = len(stages)
    for i in range(sl):
        if i == 0: #first one
            prev = stages[i]
            cumn = 1
        elif prev == stages[i]:
            cumn += 1
        elif prev < stages[i]:
            # print(cumn,(sl-lb))
            failure[prev] = round(cumn/(sl-lb),5)
            lb = i
            prev = stages[i]
            cumn = 1
    
    #last one
    if (cumn > 1) or (prev <= N): # 실패율 100% 또는 아직 처리 안된 경우
        failure[prev] = round(cumn/(sl-lb),5)

    faillist = []
    faillist.extend([(k,v) for k,v in failure.items()])
    faillist.sort(reverse=True, key=lambda x: x[1])
    
    answer = [k for (k,v) in faillist]
    
    return answer