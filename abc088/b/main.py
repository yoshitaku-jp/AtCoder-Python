N = int(input())
s = list(map(int, input().split()))

s.sort(reverse=True)
a = []
b = []

for i in range(N):
    if i % 2 == 1:
        a.append(int(s[i]))
    elif i % 2 == 0:
        b.append(int(s[i]))
ans = abs(sum(a) - sum(b))
print(ans)
