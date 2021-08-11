
# distinct permutations

from itertools import permutations
l = list(map(int,input().split()))

l = list(permutations(l))
for i in l:
    print(*i)