# read Input
l = []
while True:
    line = input()
    if line:
        l.append(line.lower())
    else:
        break

print(*l)