from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,index,vertex):
        self.graph[index].append(vertex)

    def BFS(self,start):
        visited = set()
        queue = []
        visited.add(start)
        queue.append(start)
        while queue:
            first = queue.pop(0)
            print(first)
            for x in self.graph[first]:
                if x not in visited:
                    visited.add(x)
                    queue.append(x)
        return
