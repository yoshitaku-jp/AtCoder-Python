A, B = map(int, input().split())

if A == 1 and B == 1:
    cnt = 1
elif A == 1:
    cnt = B - 2
elif B == 1:
    cnt = A - 2
else:
    cnt = (A - 2) * (B - 2)

print(cnt)
