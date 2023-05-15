import sys

k = []
d = []

for i in range(9):
    h = int(sys.stdin.readline().strip())
    k.append(h)

k.sort()

tar_num = sum(k) - 100
start = 0
end = len(k) - 1

while start < end:
    left = k[start]
    right = k[end]

    if (left + right) == tar_num:
        d.append(start)
        d.append(end)
        break
    else:
        if (left + right) < tar_num:
            start += 1
        else:
            end -= 1

for i in range(9):
    if i in d:
        continue
    print(k[i])