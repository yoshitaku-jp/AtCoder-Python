P = list(map(int, input().split()))
S = "abcdefghijklmnopqrstuvwxyz"

ans = []
for i in range(0, len(P)):
    ans.append(S[P[i] - 1])

print("".join(ans))
