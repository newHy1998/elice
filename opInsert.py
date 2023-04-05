import sys

n = int(input())
A = list(map(int, input().split(" ")))
a, s, m, d = map(int, input().split(" "))
max_size = -sys.maxsize
min_size = sys.maxsize

def dfs(num, i, add, sub, mul, div):
    global max_size, min_size
    
    if i == n:
        max_size = max(num, max_size)
        min_size = min(num, min_size)
        return
    
    if add > 0:
        dfs(num + A[i], i + 1, add - 1, sub, mul, div)
    if sub > 0:
        dfs(num - A[i], i + 1, add, sub - 1, mul, div)
    if mul > 0:
        dfs(num * A[i], i + 1, add, sub, mul - 1, div)
    if div > 0:
        if num < 0:
            dfs((abs(num) // A[i] * -1), i + 1, add, sub, mul, div - 1)
        else:
            dfs(num // A[i], i + 1, add, sub, mul, div - 1)
    
dfs(A[0], 1, a, s, m, d)

print(max_size)
print(min_size)