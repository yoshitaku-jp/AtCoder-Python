S = [input(), input(), input()]
T = input()
ans = ""
for i in range(len(T)):
    ans += S[int(T[i]) - 1]
print(ans)
