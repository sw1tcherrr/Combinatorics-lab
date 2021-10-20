file = "part2num"
with open(file + ".in", "r") as f:
    s = list(map(int, f.readline().split("+")))
n = sum(s)

d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n, 0, -1):
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


r = 0
l = 1
nc = n
for i in s:
    for j in range(l, i):
        r += d[n - j][j]
    n -= i
    l = i

with open(file + ".out", "w") as f:
    print(r, file=f)