file = "antigray"
with open(file + ".in", "r") as f:
    n = int(f.read())

def to_radix(x, r):
    res = []
    while x > 0:
        res.append(str(x % r))
        x //= r
    return ''.join(res[::-1])

def shift(x):
    return ''.join([str((int(i) + 1) % 3) for i in x])

with open(file + ".out", "w") as f:
    for i in range(3**(n-1)):
        c = to_radix(i, 3).zfill(n)
        print(c, file=f)
        c = shift(c)
        print(c, file=f)
        c = shift(c)
        print(c, file=f)