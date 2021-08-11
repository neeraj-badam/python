# Krushkals
import operator
class Pair:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w

def findParent(parent,child):
    if parent[child] == child:
        return child
    p = findParent(parent,parent[child])
    return p

n,edge = map(int,input().split())
l = []
for _ in range(edge):
    u,v,w = map(int,input().split())
    l.append(Pair(u,v,w))
print()
l = sorted(l,key=operator.attrgetter('w'))
parent = [i for i in range(n+1)]
ans = 0
for _ in l:
    u,v = _.u,_.v
    pu = findParent(parent,u)
    pv = findParent(parent,v)
    if pu != pv:
        print(u,v,_.w)
        ans += _.w
        parent[max(pu,pv)] = min(pu,pv)
    
print(ans)