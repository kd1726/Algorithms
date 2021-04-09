from collection import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self,index,vertex):
        self.graph[index].append(vertex)

    def ToposortUtil(self,vertx,visited,stack):
        visited[vertx]=True
        for i in self.graph[vertx]:
            if visited[i]==False:
                self.ToposortUtil(i,visited,stack)
        stack.append(vertx)
        return

    def TopSort(self):
        visited = [False]*(max(self.graph)+1)
        stack = []
        for i in range(len(self.graph)):
            if visited[i]==False:
                self.ToposortUtil(i,visited,stack)

        return stack[::-1]
