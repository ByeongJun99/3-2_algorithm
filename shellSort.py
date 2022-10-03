def shellSort(a, n):
    for h in range(1, n):
        h = 3*h + 1
    while h > 0:
        h = h // 3
        if h == 0:
            break
        for i in range(h+1, n+1):
            k = a[i-1]
            j = i
            while (j > h and a[j-h-1] > k):
                a[j-1] = a[j-h-1]
                j -= h
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
shellSort(a, len(a))
end_time = time.time() - start_time
print('쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)