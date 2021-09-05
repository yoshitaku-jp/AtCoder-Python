N = int(input())
S = input().split()

s = set()

for i in range(N):
    s.add(S[i])

if len(s) == 3:
    print("Three")
elif len(set(s)) == 4:
    print("Four")
