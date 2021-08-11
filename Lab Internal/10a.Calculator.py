#Calculator
class Calci:
    def perform(a,b,op):
        return eval((a+op+b))

a,b,op = map(str,input().split())
print(Calci.perform(a,b,op))