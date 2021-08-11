#Unzipping Lists

l = [(1,2),(2,3),(3,4),(4,5)]
l1,l2 = zip(*l)

print(list(l1),list(l2))