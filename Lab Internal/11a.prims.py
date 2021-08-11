#Prims
import sys
class Graph():
    def __init__(self,v) -> None:
        self.v = v
        graph = []
        for i in range(v):
            graph.append([0]*(v))
        self.graph = [[0]*v]*v
    def printMST(self,parent):
        print("Edge\tWeight\t")
        for i in range(1,self.v):
            print(parent[i],'-',i,'\t',self.graph[i][parent[i]])
    def minKey(self,key,mst):
        min = sys.maxsize
        for i in range(self.v):
            if key[i] < min and mst[i] == False:
                min = key[i]
                min_index = i
        return min_index
    def primMST(self):
        parent = [None] * (self.v)
        parent[0] = -1
        mst = [False] * (self.v)
        key = [sys.maxsize] * self.v
        key[0] = 0

        for i in range(self.v):
            u = self.minKey(key,mst)
            mst[u] = True
            for v in range(self.v):
                if self.graph[u][v] and not mst[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)
g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
  
g.primMST()