"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = [None] * 100

        def checkVisited(node):
            for i in visited:
                if (i != None and i.val == node.val):
                    return True
            return False

        def dfs(node: Optional['Node']):

            if (not checkVisited(node)):
                print("Node Val: " + str(node.val))
                print("Node neigbours: ")
                for j in node.neighbors:
                    print(j.val)
                n1 = Node(node.val, [])
                visited[node.val] = n1
                neigb = []
                for i in node.neighbors:
                    neigb.append(dfs(i))
                n1.neighbors = neigb
                
                return n1

            else:
                return visited[node.val]
                
            
             
        return dfs(node)