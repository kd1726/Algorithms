from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,index,vertex):
        self.graph[index].append(vertex)

#recursive DFS
    def _DFS_Rec(self,visited,vertex):
        visited.add(vertex)
        print(vertex)
        for x in self.graph[vertex]:
            if x not in visited:
                self._DFS_Rec(visited,x)
        return

    def DFS_Rec(self):
        visited = set()
        for x in list(self.graph):
            if x not in visited:
                self._DFS_Rec(visited,x)
        return
#iterative

     def DFS_Iter(self,vertex):
            visited = set()
            stack = []
            stack.append(vertex)
            while stack:

                first = stack.pop()

                if first not in visited:
                    visited.add(first)
                    print(first)

                for x in self.graph[first]:
                    if x not in visited:
                        stack.append(x)
            return
