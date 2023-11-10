class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        result = []
        LASTNODE = len(graph)-1
        
        def dfs(currentNode, path):

            path.append(currentNode)

            if (currentNode == LASTNODE):
                result.append(path.copy())
                path.pop()
                return

            for i in graph[currentNode]:
                dfs(i,path)

            path.pop()
            

        dfs(0, [])

        return result
