#Concatenate
s = list(map(str,input().split()))

n = int(input())
res = []
for i in s:
    for j in range(1,n+1):
        res.append(i+str(j))

print(res)