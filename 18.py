file = "brackets2num"
with open(file + ".in", "r") as f:
    s = f.readline()
n = len(s) // 2
d = [[0 for _ in range(n + 1)] for _ in range(2 * n + 1)]
d[0][0] = 1
for i in range(1, 2 * n + 1):
    for j in range(n + 1):
        if j > 0:
            d[i][j] = d[i - 1][j - 1]
        if j < n:
            d[i][j] += d[i - 1][j + 1]

b = 0
k = 0
for i in range(2 * n):
    if s[i] == "(":
        b += 1
    else:
        if 0 <= b + 1 <= n:
            k += d[2 * n - i - 1][b + 1]
        b -= 1

with open(file + ".out", "w") as f:
    print(k, file=f)