
# a,e,i,o,u

from itertools import permutations
l = ['a','e','i','o','u']

l = list(permutations(l))
for i in l:
    print(*i)