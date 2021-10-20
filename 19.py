file = "num2brackets2"
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
op = []
for i in range(2 * n - 1, -1, -1):
    t = 0
    if 0 <= b + 1 <= n:
        t = d[i][b + 1]
        if i - b - 1 > 0:
            t <<= ((i - b - 1)>>1)

    if t >= k:
        s += "("
        op.append("(")
        b += 1
        continue
    k -= t

    t = 0
    if 0 <= b - 1 <= n and op and op[-1] == "(":
        t = d[i][b - 1]
        if i - b + 1 > 0:
            t <<= ((i - b + 1)>>1)

    if t >= k:
        s += ")"
        b -= 1
        op.pop()
        continue
    k -= t

    t = 0
    if 0 <= b + 1 <= n:
        t = d[i][b + 1]
        if i - b - 1 > 0:
            t <<= ((i - b - 1)>>1)

    if t >= k:
        s += "["
        op.append("[")
        b += 1
        continue
    k -= t

    s += "]"
    b -= 1
    op.pop()

with open(file + ".out", "w") as f:
    print(s, file=f)