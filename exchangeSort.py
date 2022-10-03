def exchangeSort(a, n):
    for i in range (1, n):
        for j in range(i+1, n+1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] < a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

import random, time

N = 50000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
    #a.append(i)
start_time = time.time()
exchangeSort(a, N)
end_time = time.time() - start_time
print('교환 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)