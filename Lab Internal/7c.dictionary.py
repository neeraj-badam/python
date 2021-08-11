#dictionary
l1 = ['a','b','b','d','e']
l2 = ['1','2','3','4','5']

d = {}
for key,value in zip(l1,l2):
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)

print(d)