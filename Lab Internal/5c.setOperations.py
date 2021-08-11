#Missing and additional Values

s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))

print("Additional values in s1 and missing values in s2",s1.difference(s2))
print("Additional values in s2 and missing values in s1",s2.difference(s1))