from collections import deque

card = input().split(" ")
card_num = int(card[0])
target = int(card[1])
queue = deque()
res = []

for i in range(card_num):
    queue.append(i + 1)
    
while queue:
    queue.rotate(-target)
    res.append(queue.pop())

res = list(map(str, res))

print("<", end = '')
print(", ".join(res), end = '')
print(">")