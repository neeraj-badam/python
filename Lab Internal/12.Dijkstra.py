# Dijkstra's
import heapq as heap
import sys
class Pair:
    def __init__(self,first,second) -> None:
        self.first = first
        self.second = second
    def __lt__(self,next):
        return self.first < next.first
def dijkstra(g,source,destination):
    n = len(g)
    dis = [sys.maxsize]*(n+1)
    minHeap = []
    dis[source] = 0
    heap.heappush(minHeap,Pair(0,source))
    while len(minHeap) != 0:
        p = heap.heappop(minHeap)
        u,dt = p.second,p.first
        if u == destination :
            return dis[u]

        for pair in g[u]:
            w,v = pair.first,pair.second
            old_distance,new_distance = dis[v],dt+w
            if new_distance < old_distance:
                dis[v] = new_distance
                heap.heappush(minHeap,Pair(new_distance,v))
                heap.heapify(minHeap)

    return None
for _ in range(int(input())):
    n,edge = map(int,input().split())
    g = []
    for _ in range(n+1):
        g.append([]*(n+1))
    for _ in range(edge):
        u,v,w = map(int,input().split())
        g[u].append(Pair(w,v))
    source,destination = map(int,input().split())
    res = dijkstra(g,source,destination)
    if res == None:
        print("NO")
    else:        
        print(res)