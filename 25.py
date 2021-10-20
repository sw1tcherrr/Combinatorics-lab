file = "nextchoose"
with open(file + ".in", "r") as f:
    n, k = map(int, f.readline().split())
    s = list(map(int, f.readline().split()))

def nextt(s):
    s.append(n + 1)
    i = k - 1
    while i >= 0 and s[i + 1] - s[i] < 2:
        i -= 1
    if i >= 0:
        s[i] += 1
        for j in range(i + 1, k):
            s[j] = s[j - 1] + 1
        return s[:-1]
    return [-1]

with open(file + ".out", "w") as f:
    print(*nextt(s[:]), file=f)