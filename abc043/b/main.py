data = input()

ans = []
for i in data:

    if i != "B":
        ans.append(i)
    else:
        if len(ans) > 0:
            ans.pop()
print("".join(ans))
