class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self,index,vertex):
        self.graph[index].append(vertex)

    def is_cyclic_utils(self,vertex,visited,stack):
        visited[vertex] = True
        stack[vertex] = True
        for i in self.graph[vertex]:
            if visited[i]==False:
                if self.is_cyclic_utils(i,visited,stack) == True:
                    return True
            elif stack[i] == True:
                return True

    def cyclic(self):
        visited = [False]*(max(self.graph)+1)
        stack = [False]*(max(self.graph)+1)
        for i in range(len(self.graph)):
            if visited[i]==False:
                if self.is_cyclic_utils(i,visited,stack) == True:
                    return "Cyclic Detected"

        return False
