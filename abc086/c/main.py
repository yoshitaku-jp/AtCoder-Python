n = int(input())

t0 = 0
x0 = 0
y0 = 0

for i in range(n):
    t, x, y = map(int, input().split())
    dt = abs(x - x0) + abs(y - y0)
    time = abs(t - t0)

    t0 = t
    x0 = x
    y0 = y

    if dt > time or dt % 2 != time % 2:
        print("No")
        exit()

print("Yes")
