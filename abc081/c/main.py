N = int(input())
A = list(map(int, input().split()))

count = 0

flag = True
while flag:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] //= 2
        else:
            flag = False
    if flag:
        count += 1

print(count)
