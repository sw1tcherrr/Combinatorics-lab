file = "telemetry"
with open(file + ".in", "r") as f:
    n, k = map(int, f.readline().split())

res = [[i] for i in range(k)]
for m in range(1, n):
    l = k ** m
    rev = False
    for j in range(1, k):
        rev = not rev
        for i in range(l):
            idx = l - i - 1 if rev else i
            res.append(res[idx]+[j])
    for i in range(l):
        res[i].append(0)

with open(file + ".out", "w") as f:
    for i in res:
        print(*i, file=f, sep='')