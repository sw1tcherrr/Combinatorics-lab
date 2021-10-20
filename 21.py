file = "num2part"
with open(file + ".in", "r") as f:
    n, r = map(int, f.readline().split())

d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# d[0] = [1 for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n, -1, -1):
        if i == j:
            d[i][j] = 1
            continue
        if i < j:
            d[i][j] = 0
            continue
        if j + 1 <= n:
            d[i][j] = d[i][j + 1]
        if i - j >= 0:
            d[i][j] += d[i - j][j]

res = []
r = d[n][1] - r
while (r > 0 and n > 0):
    k = 0
    for i in range(n, -1, -1):
        if d[n][i] >= r:
            k = i
            break
    res.append(k)
    if k + 1 <= n:
        r -= d[n][k+1]
    n -= k

with open(file + ".out", "w") as f:
    print(*res, file=f, sep='+')