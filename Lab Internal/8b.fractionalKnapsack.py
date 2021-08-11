#Knapsack
import operator
class Pair:
    def __init__(self,w,v) -> None:
        self.w,self.v,self.vByw = w,v,v/w
def knapsack(l,c):
    profit = 0
    for _ in l:
        w = _.w
        if c-w>=0:
            profit += _.v
            c -= w
        else:
            profit += c*_.v/w
            break
    return profit
wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
l = []
for i,j in zip(wt,val):
    l.append(Pair(i,j))
bagCapacity = 50
l = sorted(l,key=operator.attrgetter('vByw'),reverse=True)
res =knapsack(l,bagCapacity)
print(res)