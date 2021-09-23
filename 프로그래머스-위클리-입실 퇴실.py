def solution(enter, leave):
    answer = [0]*len(enter)
    room = []

    for e in enter:
        room.append(e)
        
        for i in room[:-1]:
            answer[e-1] += 1
            answer[i-1] += 1
        
        while leave:
            o = leave[0]
            if o in room:
                room.remove(o)
                leave.remove(o)
            else:
                break
    
    return answer