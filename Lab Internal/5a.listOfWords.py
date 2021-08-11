#listOfWords

def function(s,l):
    return [string for string in s if len(string)>l]

s = list(map(str,input().split()))
n = int(input())

res = function(s,n)

print(res)