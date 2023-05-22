import sys
import heapq

v, e = map(int, input().split(" "))
start = int(input()) - 1
dist = [float("inf")] * v
dist[start] = 0

heap = []
matrix = [[] for i in range(v)]

for i in range(e):
    a, b, w = map(int, sys.stdin.readline().strip().split(" "))
    matrix[a - 1].append((b - 1, w))

heapq.heappush(heap, (0, start))

while heap:
    cur_distance, cur_node = heapq.heappop(heap)
    if dist[cur_node] < cur_distance:
        continue
    for to_node, to_distance in matrix[cur_node]:
        d = cur_distance + to_distance
        if dist[to_node] > d:
            dist[to_node] = d
            heapq.heappush(heap, (d, to_node))

for i in dist:
    if i != float("inf"):
        print(i)
    else:
        print("INF")