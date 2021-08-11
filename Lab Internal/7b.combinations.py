#Combinations
from itertools import product

d = dict({'2':['a','b'],'3':['c','d','e'],'4':['p','q','r','s']})

for combo in product(*(d[k] for k in d.keys())):
    print(combo)