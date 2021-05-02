# queue를 truck_weights가 아니라, 다리에 올라갈 수 있는 트럭 큐 queue를 새로이 만들어 사용하는 것이 핵심
# deque로 popleft를 하면 오히려 시간초과

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    length=[0]*bridge_length
    truck_weights=deque(truck_weights)

    while length:
        answer+=1
        length.pop(0)
        if truck_weights:
            if sum(length)+truck_weights[0]<=weight:
                length.append(truck_weights.popleft())
            else:
                length.append(0)
    return answer