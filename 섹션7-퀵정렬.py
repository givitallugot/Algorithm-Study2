# 퀵정렬: 전위순회 (본연의 일을 먼저)
# pivot 맨 마지막 값을 중심값 pivot으로 두고, 작으면 왼쪽으로 크면 오른쪽으로

def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i] # SWAP
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print('Before sort: ', end = '')
    print(arr)
    Qsort(0,9) # 0번부터 7번까지 정렬
    print()
    print('After sort: ', end = '')
    print(arr) 