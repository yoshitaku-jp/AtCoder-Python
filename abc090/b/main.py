A, B = map(int, input().split())

count = 0
for i in range(A, B + 1):
    if str(i) == "".join(list(reversed(str(i)))):
        count += 1
print(count)
