from typing import List


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

for i in range(n):
    result += a[i]*b[i]

print(result)