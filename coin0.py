from sys import stdin

n, k = list(map(int, input().split(" ")))
coin_list = []
for i in range(n):
    coin_list.append(int(stdin.readline().strip()))

count = 0

for coin in reversed(coin_list):
    if k == 0:
        break
    if coin <= k:
        mok = k // coin
        count += mok
        k -= coin * mok
        
print(count)