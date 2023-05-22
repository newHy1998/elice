from collections import deque

s = []

def tracking(s):
    if len(s) == m:
        print(" ".join(list(map(str, s))))
        return
    for i in range(1, n + 1):
        if i in s:
            continue
        else:
            s.append(i)
            tracking(s)
            s.pop()

n, m = map(int, input().split(" "))
tracking(s)

