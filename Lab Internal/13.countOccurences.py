# countOccurences
f = open('sample.txt','r')
fr = f.read()

l = fr.split()
res = 0
for i in l:
    res += 1 if i == "Hey" else 0
print(res)