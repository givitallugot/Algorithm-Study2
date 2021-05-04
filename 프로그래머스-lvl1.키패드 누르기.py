def solution(numbers, hand):
    answer = ''
    keypad = [(3,1), 
              (0,0), (0,1), (0,2),
              (1,0), (1,1), (1,2),
              (2,0), (2,1), (2,2),
              (3,0),  (3,2)] # index가 키패드 번호를 나타내도록, 10, 11이 초기값
    
    lhloc = keypad[10]  # left hand location
    rhloc = keypad[11] # right hand location
    
    for k in numbers:
        if k in [1,4,7]:
            lhloc = keypad[k]
            answer += 'L'
        elif k in [3,6,9]:
            rhloc = keypad[k]
            answer += 'R'
        else:
            ld = abs(keypad[k][0] - lhloc[0]) + abs(keypad[k][1] - lhloc[1])
            rd = abs(keypad[k][0] - rhloc[0]) + abs(keypad[k][1] - rhloc[1])

            if ld < rd:
                lhloc = keypad[k]
                answer += 'L'
            elif rd < ld:
                rhloc = keypad[k]
                answer += 'R'
            else:
                if hand == "left":
                    lhloc = keypad[k]
                    answer += 'L'
                else:
                    rhloc = keypad[k]
                    answer += 'R'
    
    return answer