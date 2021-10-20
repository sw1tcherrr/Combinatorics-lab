file = "partition"
with open(file + ".in", "r") as f:
    n = int(f.read())

res = []
def gen(p, m, k):
    if k <= 0 and m != 0:
        return
    if m == 0:
        res.append(p)
        return

    if k <= m:
        gen(p + [k], m - k, k - 2)
    gen(p, m, k - 2)

gen([], n, n)

with open(file + ".out", "w") as f:
    for i in res:
        print(*i[::-1], file=f, sep='+')