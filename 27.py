file = "nextbrackets"
with open(file + ".in", "r") as f:
    s = list(f.read().strip())

cnt_o = 0
cnt_c = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == "(":
        cnt_o += 1
        if cnt_c > cnt_o:
            break
    else:
        cnt_c += 1
end = len(s) - cnt_o - cnt_c
if end == 0:
    s = "-"
else:
    s[end] = ")"
    end += 1
    for i in range(cnt_o):
        s[end] = "("
        end += 1
    for i in range(cnt_c - 1):
        s[end] = ")"
        end += 1

with open(file + ".out", "w") as f:
    print(*s, file=f, sep="")