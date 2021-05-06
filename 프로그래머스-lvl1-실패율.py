## 100점 ##
def solution(N, stages):
    answer = []
    stages.sort()
    S = dict()
    F = dict()
    R = dict()

    # dict initialize
    for i in range(1, N+1):
        S[i] = 0
        F[i] = 0
        R[i] = -1

    for j in stages:
        for k in range(1, min(j+1, N+1)):
            S[k] += 1
        if j <= N:
            F[j] += 1

    # print(S)
    # print(F)

    for s in range(1, N+1):
        if S[s] == 0:
            R[s] = 0
        else:
            R[s] = F[s]/S[s]

    R = sorted(R.items(), key=lambda x: x[1], reverse=True)

    answer.extend([k for k,v in R])
    return answer


## 37점 ## 

def solution2(N, stages):
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

    print(failure)
    #last one
    print(cumn, prev)
    if (cumn > 1) or (prev <= N): # 실패율 100% 또는 아직 처리 안된 경우
        failure[prev] = round(cumn/(sl-lb),5)

    faillist = []
    faillist.extend([(k,v) for k,v in failure.items()])
    faillist.sort(reverse=True, key=lambda x: x[1])

    answer = [k for (k,v) in faillist]

    return answer
