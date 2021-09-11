from collections import Counter
from itertools import combinations

S = Counter()
N = int(input())

for i in range(N):
    S[input()[0]] += 1
print(sum(S[a] * S[b] * S[c] for a, b, c in combinations("MARCH", 3)))
