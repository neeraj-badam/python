# removeEmptyTuples

t = [(),(1,),(1,2,3),(1,4,5),()]
res = filter(None,t)
print(list(res))

res = [l for l in t if len(l) > 0]
print(res)