#Quick Sort

def QS(a,l,h):
    if l < h:
        p = partition(a,l,h)

        QS(a,l,p-1)
        QS(a,p+1,h)
    
def partition(a,l,h):
    pivot = l

    while l < h:
        while l<len(a) and a[l] <= a[pivot]:
            l+=1
        while a[h] > a[pivot]:
            h -= 1
        
        if l < h:
            a[l],a[h] = a[h],a[l]

    a[h],a[pivot] = a[pivot],a[h]

    return h

a = [ 10, 7, 8, 9, 1, 1]
h = len(a)-1
QS(a,0,h)
print(a)