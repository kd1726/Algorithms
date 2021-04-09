#detecting a cycle in an undirected graph
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,index,vertex):
        self.graph[index].append(vertex)

    def _detect_undirected_cycle(self,vertex,visited,parent):
        visited.add(vertex)
        for x in self.graph[vertex]:
            if x not in visited:
                self._detect_undirected_cycle(self,x,visited,vertex)
                return True
            elif parent!=x:
                return True
        return False

    def detect_undirected_cycle(self):
        visited = set()
        for x in list(self.graph):
            if self._detect_undirected_cycle(self,x,visited,-1)==True:
                return True
        return False
