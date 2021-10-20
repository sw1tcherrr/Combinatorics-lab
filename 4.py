file = "chaincode"
with open(file + ".in", "r") as f:
    n = int(f.read())

codes = ['0' * n]
hashes = {0}
for i in range(2**n - 1):
    p = codes[-1][1:]
    if not p:
        ph = 0
    else:
        ph = int(p, 2)

    if (ph * 2 + 1) not in hashes:
        codes.append(p + '1')
        hashes.add(ph * 2 + 1)
    else:
        codes.append(p + '0')
        hashes.add(ph * 2)

with open(file + ".out", "w") as f:
    for c in codes:
        print(c, file=f)