from collections import deque
import sys

m, n = list(map(int, input().split(" ")))
matrix = [[0] * m for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
breaker = False

for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    for j, b in enumerate(line):
        matrix[i][j] = int(b)
        
queue = deque()            
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])
        
while queue:
    x, y = queue.popleft()
            
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
                
        if 0 <= mx < n and 0 <= my < m:
            if matrix[mx][my] == 0:
                matrix[mx][my] = matrix[x][y] + 1
                queue.append([mx, my])       
                
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            breaker == True
            exit(0)
if breaker == False:
    print(max(map(max, matrix)) - 1)