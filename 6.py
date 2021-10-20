file = "vectors"
with open(file + ".in", "r") as f:
    n = int(f.read())

res = []
def gen(p):
    if len(p) == n:
        res.append(p)
        return

    gen(p + "0")
    if not p or p[-1] == "0":
        gen(p + "1")
gen("")

with open(file + ".out", "w") as f:
    print(len(res), file=f)
    for i in res:
        print(i, file=f)