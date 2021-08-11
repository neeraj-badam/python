#password regex
import re

s = input()

spl = re.findall("[@#$]",s)
small = re.findall("[a-z]",s)
big = re.findall("[A-Z]",s)
l = len(s)
l = l >= 6 and l <= 16

if l and big and small and spl:
    print("Valid passowrd")
else:
    print("Invalid passowrd")