def insertionSort(a, n):
    for i in range(2, n+1):
        j = i
        k = a[i-1]
        while a[j-2] > k:
            a[j-1] = a[j-2]
            j = j - 1
        a[j-1] = k
    return a

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

N = 5000
a = [-1]    # 처음에 더미값으로 -1을 넣어줌
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
insertionSort(a, len(a))
end_time = time.time() - start_time
print('삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)