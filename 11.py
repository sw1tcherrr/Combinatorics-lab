file = "subsets"
with open(file + ".in", "r") as f:
    n = int(f.read())

res = []
used = [0 for i in range(n + 1)]
def gen(p, k):
    res.append(p)
    if len(p) == n:
        return

    for i in range(k + 1, n + 1):
        if not used[i]:
            used[i] = 1
            gen(p + [i], i)
            used[i] = 0

gen([], 0)

with open(file + ".out", "w") as f:
    for i in res:
        print(*i, file=f)