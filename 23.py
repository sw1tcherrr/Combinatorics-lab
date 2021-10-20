file = "nextvector"
with open(file + ".in", "r") as f:
    v = f.read().strip()

n = len(v)


def nextt(s):
    v = list(s)
    for i in range(n - 1, -1, -1):
        if v[i] == "1":
            v[i] = "0"
        else:
            v[i] = "1"
            return "".join(v)
    return "-"


def prev(s):
    v = list(s)
    for i in range(n - 1, -1, -1):
        if v[i] == "0":
            v[i] = "1"
        else:
            v[i] = "0"
            return "".join(v)
    return "-"

with open(file + ".out", "w") as f:
    print(prev(v), file=f)
    print(nextt(v), file=f)