import sys
import heapq

T = int(input())
res = [[] for i in range(T)]

for i in range(T):
    n, m, t = map(int, input().split(" "))
    s, g, h = map(int, input().split(" "))
    matrix = [[] for i in range(n)]
    heap = []
    s -= 1
    g -= 1
    h -= 1
    dt = []

    for j in range(m):
        a, b, d = map(int, sys.stdin.readline().strip().split(" "))
        if (a - 1, b - 1) == (g, h) or (a - 1, b - 1) == (h, g):
            matrix[a - 1].append((b - 1, d * 2 - 1))
            matrix[b - 1].append((a - 1, d * 2 - 1))
        else:
            matrix[a - 1].append((b - 1, d * 2))
            matrix[b - 1].append((a - 1, d * 2))

    for l in range(t):
        dt.append(int(input()) - 1)
    dt.sort()

    dist = [float("inf")] * n
    dist[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        cur_distance, cur_node = heapq.heappop(heap)
        if dist[cur_node] < cur_distance:
            continue
        for to_node, to_distance in matrix[cur_node]:
            d = cur_distance + to_distance
            if dist[to_node] > d:
                dist[to_node] = d
                heapq.heappush(heap, (d, to_node))

    for j in dt:
        if dist[j] % 2 == 1:
            res[i].append(j + 1)

for i in res:
    for j in i:
        print(j, end = " ")

    print()