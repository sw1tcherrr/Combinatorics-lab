file = "nextperm"
with open(file + ".in", "r") as f:
    n = int(f.readline())
    s = list(map(int, f.readline().split()))

def nextt(s):
    for i in range(n - 2, -1, -1):
        if s[i] < s[i + 1]:
            m = i + 1
            for j in range(i + 1, n):
                if s[j] < s[m] and s[j] > s[i]:
                    m = j
            s[i], s[m] = s[m], s[i]
            s[i + 1:] = s[n - 1:i:-1]
            return s

    return [0]*n


def prev(s):
    for i in range(n - 2, -1, -1):
        if s[i] > s[i + 1]:
            m = i + 1
            for j in range(i + 1, n):
                if s[j] > s[m] and s[j] < s[i]:
                    m = j
            s[i], s[m] = s[m], s[i]
            s[i + 1:] = s[n - 1:i:-1]
            return s

    return [0]*n

with open(file + ".out", "w") as f:
    print(*prev(s[:]), file=f)
    print(*nextt(s[:]), file=f)