def quickSort(a, l, r):
    if r > l:
        i = partition(a, l, r)
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)
    return a

def partition(a, l, r):
    k = a[r-1]
    i = l
    j = r - 1
    while True:
        while a[i-1] < k:
            i = i + 1
        while a[j-1] > k:
            j = j - 1
        if i >= j:
            break
        a[i-1], a[-1] = a[j-1], a[i-1]
    a[i-1], a[r-1] = a[r-1], a[i-1]
    return i


def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

import random, time

N = 10
a = [-1]    # 처음에 더미값으로 -1을 넣어줌
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
quickSort(a, 1, len(a))
end_time = time.time() - start_time
print('퀵 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)