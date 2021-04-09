#detecting a cycle in an undirected graph
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,index,vertex):
     self.graph[index].append(vertex)
     self.graph[vertex].append(index)

    def _detect_undirected_cycle(self,vertex,visited,parent):
        visited.add(vertex)
        for x in self.graph[vertex]:
            if x not in visited:
                self._detect_undirected_cycle(x,visited,vertex)
                return False
            elif parent==x:
                return True
        return False

    def detect_undirected_cycle(self):
        visited = set()
        for x in list(self.graph):
            if self._detect_undirected_cycle(x,visited,-1)==True:
                return True
        return False
