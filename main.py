def digit(d, k):
    a = d // (10^k)
    return a % 10

print(digit(123456789, 3))