def DFS(numbers, n, result, target):
    global count

    if len(numbers) == n:
        if result == target:
            count += 1
        return
    else:
        DFS(numbers, n+1, result + numbers[n-1], target) # , numstr+'+'+str(numbers[n-1])
        DFS(numbers, n+1, result - numbers[n-1], target)

count = 0
def solution(numbers, target):
    global count
    answer = 0
    DFS(numbers, 0, 0, target)
    answer = count
    return answer