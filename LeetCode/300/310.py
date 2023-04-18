class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
          return [0]
        
        adjacent = [set() for _ in range(n)]
        for i, j in edges:
          adjacent[i].add(j)
          adjacent[j].add(i)
        
        leaves = [i for i in range(n) if len(adjacent[i]) == 1]

        while n > 2:
          print(n, leaves)
          n -= len(leaves)
          newLeaves = []
          for i in leaves:
            j = adjacent[i].pop()
            adjacent[j].remove(i)
            if len(adjacent[j]) == 1:
              newLeaves.append(j)
          leaves = newLeaves
        return leaves
