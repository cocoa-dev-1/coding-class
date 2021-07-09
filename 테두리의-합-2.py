n = int(input())
answer = sum(range(1, n+1)) + sum(range(1, 1+(n*(n-1))+1, n)) + sum(range(1+(n*(n-1)), n*n+1)) + sum(range(n, (n*n)+1, n))
answer -= 2*(n*n+1)
print(answer)