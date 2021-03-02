n = int(input())
data = list(map(int, input().split()))

base = round(sum(data) / len(data))

ans = 0
for i in range(n):
    ans += (data[i] - base) ** 2

print(ans)
