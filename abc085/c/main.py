N, Y = map(int, input().split())

ans1, ans2, ans3 = 0, 0, 0

for x in range(N + 1):
    for y in range(N + 1 - x):
        z = N - x - y
        if x * 10 + y * 5 + z == Y / 1000:
            ans1, ans2, ans3 = x, y, z


print(f"{ans1} {ans2} {ans3}" if ans1 + ans2 + ans3 > 0 else "-1 -1 -1")
