file = "choose2num"
with open(file + ".in", "r") as f:
    n, k = map(int, f.readline().split())
    z = list(map(int, f.readline().split()))

m = 0
c = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
    c[i][0] = 1
for i in range(1, n+1):
    for j in range(1, k+1):
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]


def gen(p):
    global m
    if len(p) == k:
        if p == z:
            return
        m += 1

    for i in range(1 if not p else p[-1] + 1, n - k + len(p) + 2):
        t = c[n - i][k - len(p) - 1]
        if p + [i] == z[:len(p) + 1]:
            gen(p + [i])
            return
        else:
            m += t

gen([])

with open(file + ".out", "w") as f:
    print(m, file=f)