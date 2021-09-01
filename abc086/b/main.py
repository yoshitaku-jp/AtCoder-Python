A, B = map(int, input().split())

if (int(str(A) + str(B)) ** 0.5).is_integer():
    print("Yes")
else:
    print("No")
