# Case 1. 틀림, 최적의 위치가 주로 시청자들의 재생 시작 시간에만 한정되지 않음 => 모든 초 단위에서 확인해야 함

def TimetoNum(time):
    H, M, S = map(int,time.split(sep = ':'))
    return H*3600 + M*60 + S

def NumtoTime(num):
    H=str(num//3600); M=str((num%3600)//60); S=str((num%3600)%60)
    H=H.rjust(2, '0'); M=M.rjust(2, '0'); S=S.rjust(2, '0')
    return H+':'+M+':'+S

def solution(play_time, adv_time, logs):
    answer = ''
    logs.sort()

    logs_num = []
    for log in logs:
        s, e = map(TimetoNum, log.split(sep='-'))
        logs_num.append((s,e))
        
    # print(start, end)
    play_num = TimetoNum(play_time)
    adv_num = TimetoNum(adv_time)
    smax = 0
    
    if play_num-logs_num[0][0] <= adv_num:
        answer = NumtoTime(play_num - adv_num)
    else:
        for i in range(len(logs_num)):
            adv_end = logs_num[i][0] + adv_num
            lsum = 0
            # adv_start = logs_num[i][0]
            for log_n in logs_num[i:]:
                if log_n[0] <= adv_end:
                    lsum += abs(min(log_n[1], adv_end) - log_n[0])

            if smax < lsum:
                smax = lsum
                print(NumtoTime(logs_num[i][0]))
                answer = NumtoTime(logs_num[i][0])

    return answer

# Case 2. Memoization, 동적 계획법을 이용해야 함.
def TimetoNum(time):
    H, M, S = map(int,time.split(sep = ':'))
    return H*3600 + M*60 + S

def NumtoTime(num):
    H=str(num//3600); M=str((num%3600)//60); S=str((num%3600)%60)
    H=H.rjust(2, '0'); M=M.rjust(2, '0'); S=S.rjust(2, '0')
    return H+':'+M+':'+S

def solution(play_time, adv_time, logs):
    play_time = TimetoNum(play_time)
    adv_time = TimetoNum(adv_time)
    play = [0 for i in range(play_time + 1)]
        
    for log in logs:
        s, e = map(TimetoNum, log.split(sep='-'))
        play[s] += 1 # 시작에는 +1
        play[e] -= 1 # 시작에는 -1
    
    for i in range(1, len(play)): # 구간별 시청자 수 누적
        play[i] = play[i] + play[i-1]
        
    for i in range(1, len(play)): # 전체 시청자 수 누적
        play[i] = play[i] + play[i-1]
    
    play_max = 0
    max_time = 0
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            temp = play[i] - play[i-adv_time] # 해당 구간에서 시청자 수를 구한 것
        else:
            temp = play[i]
            
        if play_max < temp:
            play_max = temp
            max_time = i-adv_time+1
            
    answer = NumtoTime(max_time)
    return answer