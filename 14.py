file = "perm2num"
with open(file + ".in", "r") as f:
    n = int(f.readline())
    z = list(map(int, f.readline().split()))

k = 0
used = [0 for i in range(n + 1)]
fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000]
def gen(p):
    global k
    if len(p) == n:
        if p == z:
            return
        k += 1

    for i in range(1, n + 1):
        if not used[i]:
            if p + [i] == z[:len(p) + 1]:
                used[i] = 1
                gen(p + [i])
            else:
                k += fact[n - len(p) - 1]
gen([])

with open(file + ".out", "w") as f:
    print(k, file=f)