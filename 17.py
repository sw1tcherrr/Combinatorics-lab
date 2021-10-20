file = "num2brackets"
with open(file + ".in", "r") as f:
    n, k = map(int, f.readline().split())

d = [[0 for _ in range(n + 1)] for _ in range(2 * n + 1)]
d[0][0] = 1
for i in range(1, 2 * n + 1):
    for j in range(n + 1):
        if j > 0:
            d[i][j] = d[i - 1][j - 1]
        if j < n:
            d[i][j] += d[i - 1][j + 1]

k += 1
b = 0
s = ""
for i in range(2 * n - 1, -1, -1):
    if 0 <= b + 1 <= n and d[i][b + 1] >= k:
        s += "("
        b += 1
    else:
        if 0 <= b + 1 <= n:
            k -= d[i][b + 1]
        s += ")"
        b -= 1
with open(file + ".out", "w") as f:
    print(s, file=f)