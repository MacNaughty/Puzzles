import unittest
from collections import deque, defaultdict


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = dict()

        def dfs(curr):
            if not curr:
                return None

            if curr in clone_map:
                return clone_map[curr]
            else:
                clone = Node(curr.val)
                clone_map[curr] = clone

                clone.neighbors = []

                for neighbor in curr.neighbors:
                    if neighbor:
                        clone.neighbors.append(dfs(neighbor))

                return clone

        return dfs(node)
    
    
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # Dictionary to map original nodes to their clones
        clone_map = {node: Node(node.val)}

        # Use a queue to perform BFS
        q = deque([node])

        while q:
            curr = q.popleft()

            # Iterate through all the neighbors of the current node
            for neighbor in curr.neighbors:
                # If the neighbor hasn't been cloned yet, clone it
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # Link the clone of the current node to the clone of its neighbor
                clone_map[curr].neighbors.append(clone_map[neighbor])

        # Return the clone of the original root node
        return clone_map[node]







class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
