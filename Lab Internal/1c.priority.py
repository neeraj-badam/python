#priority of operators
def priority(c):
    if c in ['+','-']:
        return 1
    else:
        return 2

print(priority('/'))