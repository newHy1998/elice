from sys import stdin

A, B, C = map(int, stdin.readline().strip().split(" "))

if C <= B:
    print(-1)
else:
    print(int((A//(C-B))+1))