file = "permutations"
with open(file + ".in", "r") as f:
    n = int(f.read())

res = []
used = [0 for i in range(n + 1)]
def gen(p):
    if len(p) == n:
        res.append(p)
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = 1
            gen(p + [i])
            used[i] = 0

gen([])

with open(file + ".out", "w") as f:
    for i in res:
        print(*i, file=f)