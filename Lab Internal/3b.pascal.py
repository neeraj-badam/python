#pascal triangle
def pascal(n):
    if n <= 0:
        return [[]]
    if n == 1:
        return [[1]]
    res = [[1]]
    for i in range(1,n):
        prev = res[i-1]
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(prev[j-1]+prev[j])
        res.append(temp)
    return res

n = int(input())
res = pascal(n)

for i in res:
    print(*i)