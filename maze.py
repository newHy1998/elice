from collections import deque
import sys

n, m = list(map(int, input().split(" ")))
matrix = [[0] * m for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    line = sys.stdin.readline().strip()
    for j, b in enumerate(line):
        matrix[i][j] = int(b)
        
queue = deque()
queue.append([0, 0])

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        
        if 0 <= mx < n and 0 <= my < m:
            if matrix[mx][my] == 1:
                matrix[mx][my] = matrix[x][y] + 1
                queue.append([mx, my])
    
print(matrix[n - 1][m - 1])