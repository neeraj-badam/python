#Merge Sort
def MS(a,l,h):
    if l < h:
        m = (l+h)//2

        MS(a,l,m)
        MS(a,m+1,h)
        merge(a,l,m,h)

def merge(a,l,m,h):
    p1,p2 = l,m+1

    res = [0] * (h-l+1)
    i = 0
    while p1 <= m and p2 <= h:
        if a[p1] < a[p2]:
            res[i] = a[p1]
            p1 += 1
        else:
            res[i] = a[p2]
            p2 += 1
        i += 1
    
    while p1 <= m:
        res[i] = a[p1]
        p1 += 1
        i += 1

    while p2 <= h:
        res[i] = a[p2]
        p2 += 1
        i += 1

    for i in range(l,h+1):
        a[i] = res[i-l]

a = [11,15,1,5,9,9]
MS(a,0,len(a)-1)
print(a)