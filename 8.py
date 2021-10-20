file = "choose"
with open(file + ".in", "r") as f:
    n, k = map(int, f.readline().split())

res = []
def gen(p):
    if len(p) == k:
        res.append(p)
        return

    for i in range(1 if not p else p[-1] + 1, n - k + len(p) + 2):
        gen(p + [i])

gen([])

with open(file + ".out", "w") as f:
    for i in res:
        print(*i, file=f)