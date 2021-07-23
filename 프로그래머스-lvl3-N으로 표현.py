# 너무 어려운 메모이제이션

def solution(N, number):
    answer = -1
    dp = []

    for i in range(1,9):
    # i = N의 개수
        all_case = set()
        check_number = int(str(N)* i)
        # {N}, {NN} , {NNN}...
        all_case.add(check_number)

        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1] :
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)

        if number in all_case:
            answer = i
            break

        dp.append(all_case) 
        

    return answer

# https://velog.io/@j_user0719/N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-PYTHON 참고
# 동적 계획법 문제 더 풀기..
     