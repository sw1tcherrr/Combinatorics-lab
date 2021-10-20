file = "brackets"
with open(file + ".in", "r") as f:
    n = int(f.read())

res = []
def gen(p, b):
    if len(p) == 2 * n:
        res.append(p)
        return

    if b + 1 <= 2 * n - len(p) - 1:
        gen(p + "(", b + 1)
    if b > 0:
        gen(p + ")", b - 1)

gen("", 0)

with open(file + ".out", "w") as f:
    for i in res:
        print(*i, file=f, sep='')