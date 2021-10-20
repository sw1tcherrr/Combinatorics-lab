file = "nextmultiperm"
with open(file + ".in", "r") as f:
    n = int(f.readline())
    s = list(map(int, f.readline().split()))

def nextt(s):
    for i in range(n - 2, -1, -1):
        if s[i] < s[i + 1]:
            m = i + 1
            while m < n - 1 and s[m + 1] > s[i]:
                m += 1
            s[i], s[m] = s[m], s[i]
            s[i + 1:] = s[n - 1:i:-1]
            return s

    return [0]*n

with open(file + ".out", "w") as f:
    print(*nextt(s[:]), file=f)