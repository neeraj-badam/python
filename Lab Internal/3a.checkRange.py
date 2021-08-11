#Number in a range
def checkRange(n,l,h):
    return n>=l and n<=h

n,l,h = map(int,input("Enter n,low,max range : ").split())

print(checkRange(n,l,h))