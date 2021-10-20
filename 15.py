file = "num2choose"
with open(file + ".in", "r") as f:
    n, k, m = map(int, f.readline().split())

res = []
c = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
    c[i][0] = 1
for i in range(1, n+1):
    for j in range(1, k+1):
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]


def gen(p):
    global res, m
    if len(p) == k:
        res = p
        m -= 1
        return

    for i in range(1 if not p else p[-1] + 1, n - k + len(p) + 2):
        t = c[n - i][k - len(p) - 1]
        if m >= t:
            m -= t
        else:
            gen(p + [i])
            if m < 0:
                return

gen([])

with open(file + ".out", "w") as f:
    print(*res, file=f)