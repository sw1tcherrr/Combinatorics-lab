file = "allvectors"
with open(file + ".in", "r") as f:
    n = int(f.read())
with open(file + ".out", "w") as f:
    for i in range(2**n):
        print(bin(i)[2:].zfill(n), file=f)