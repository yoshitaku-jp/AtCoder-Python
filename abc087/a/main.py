X = int(input())
A = int(input())
B = int(input())

ans = X - A
while True:
    if ans < B:
        break
    ans = ans - B

print(ans)
