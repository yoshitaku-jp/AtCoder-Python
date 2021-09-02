s = set()
for _ in range(int(input())):
    s.add(input())
ans = list(s)
ans.sort()
print(len(ans))
