"""
Graph Algorithms - Graph Traversal and Pathfinding

This module contains implementations of common graph algorithms
used in coding interviews, integrating with existing library implementations.

Common Use Cases:
- Graph traversal (DFS, BFS)
- Shortest path algorithms
- Cycle detection
- Topological sorting
- Connected components
- Minimum spanning tree
"""

from typing import List, Dict, Set, Optional, Tuple, Deque
from collections import defaultdict, deque
import heapq
import sys
import os

# Add Libs directory to path to import existing implementations
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../Libs'))
from dijkstra import Graph as DijkstraGraph, Dijkstra
from union_find import UnionFind


class Graph:
    """
    Graph representation using adjacency list.
    Supports both directed and undirected graphs.
    """
    
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        """Add edge from u to v with optional weight."""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_vertices(self):
        """Get all vertices in the graph."""
        vertices = set()
        for u in self.graph:
            vertices.add(u)
            for v, _ in self.graph[u]:
                vertices.add(v)
        return list(vertices)
    
    def get_edges(self):
        """Get all edges in the graph."""
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                if self.directed or u <= v:  # Avoid duplicates for undirected
                    edges.append((u, v, weight))
        return edges


def dfs_recursive(graph: Dict[int, List[int]], start: int, visited: Set[int] = None) -> List[int]:
    """
    Depth-First Search (recursive implementation).
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        visited: Set of visited vertices
        
    Returns:
        List of vertices in DFS order
        
    Time: O(V + E), Space: O(V)
    """
    if visited is None:
        visited = set()
    
    result = []
    
    def dfs(vertex):
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor, _ in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(start)
    return result


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Depth-First Search (iterative implementation).
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        
    Returns:
        List of vertices in DFS order
        
    Time: O(V + E), Space: O(V)
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack (reverse order for consistent traversal)
            for neighbor, _ in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Breadth-First Search implementation.
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        
    Returns:
        List of vertices in BFS order
        
    Time: O(V + E), Space: O(V)
    """
    visited = set()
    queue = deque([start])
    result = []
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor, _ in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def shortest_path_bfs(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find shortest path between two vertices using BFS (unweighted graph).
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        end: Target vertex
        
    Returns:
        Shortest path as list of vertices, None if no path exists
        
    Time: O(V + E), Space: O(V)
    """
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor, _ in graph.get(vertex, []):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None


def has_cycle_directed(graph: Dict[int, List[int]]) -> bool:
    """
    Detect cycle in directed graph using DFS.
    
    Args:
        graph: Adjacency list representation of directed graph
        
    Returns:
        True if cycle exists, False otherwise
        
    Time: O(V + E), Space: O(V)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)
    
    def dfs(vertex):
        if color[vertex] == GRAY:
            return True  # Back edge found, cycle detected
        
        if color[vertex] == BLACK:
            return False  # Already processed
        
        color[vertex] = GRAY
        
        for neighbor, _ in graph.get(vertex, []):
            if dfs(neighbor):
                return True
        
        color[vertex] = BLACK
        return False
    
    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True
    
    return False


def has_cycle_undirected(graph: Dict[int, List[int]]) -> bool:
    """
    Detect cycle in undirected graph using DFS.
    
    Args:
        graph: Adjacency list representation of undirected graph
        
    Returns:
        True if cycle exists, False otherwise
        
    Time: O(V + E), Space: O(V)
    """
    visited = set()
    
    def dfs(vertex, parent):
        visited.add(vertex)
        
        for neighbor, _ in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True  # Back edge to non-parent
        
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, -1):
                return True
    
    return False


def topological_sort(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    Topological sort of directed acyclic graph (DAG).
    
    Args:
        graph: Adjacency list representation of directed graph
        
    Returns:
        Topologically sorted vertices, None if cycle exists
        
    Time: O(V + E), Space: O(V)
    """
    # Calculate in-degrees
    in_degree = defaultdict(int)
    vertices = set()
    
    for u in graph:
        vertices.add(u)
        for v, _ in graph[u]:
            vertices.add(v)
            in_degree[v] += 1
    
    # Initialize queue with vertices having in-degree 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor, _ in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all vertices are processed (no cycle)
    return result if len(result) == len(vertices) else None


def connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find all connected components in undirected graph.
    
    Args:
        graph: Adjacency list representation of undirected graph
        
    Returns:
        List of connected components, each component is a list of vertices
        
    Time: O(V + E), Space: O(V)
    """
    visited = set()
    components = []
    
    def dfs(vertex, component):
        visited.add(vertex)
        component.append(vertex)
        
        for neighbor, _ in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor, component)
    
    vertices = set()
    for u in graph:
        vertices.add(u)
        for v, _ in graph[u]:
            vertices.add(v)
    
    for vertex in vertices:
        if vertex not in visited:
            component = []
            dfs(vertex, component)
            components.append(component)
    
    return components


def dijkstra_shortest_path(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Dijkstra's algorithm for shortest paths (integrates with existing implementation).
    
    Args:
        graph: Adjacency list with weights
        start: Starting vertex
        
    Returns:
        Dictionary mapping vertex to shortest distance from start
        
    Time: O((V + E) log V), Space: O(V)
    """
    # Convert to DijkstraGraph format
    dijkstra_graph = DijkstraGraph()
    for u in graph:
        for v, weight in graph[u]:
            dijkstra_graph.add_edge(u, v, weight)
    
    # Run Dijkstra's algorithm
    dijkstra = Dijkstra(dijkstra_graph, start)
    
    # Convert result format
    distances = {}
    for vertex in dijkstra_graph.get_nodes():
        distances[vertex] = dijkstra.shortest_distance(vertex)
    
    return distances


def kruskal_mst(edges: List[Tuple[int, int, int]], num_vertices: int) -> List[Tuple[int, int, int]]:
    """
    Kruskal's algorithm for Minimum Spanning Tree (uses existing UnionFind).
    
    Args:
        edges: List of (u, v, weight) tuples
        num_vertices: Number of vertices
        
    Returns:
        List of edges in MST
        
    Time: O(E log E), Space: O(V)
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize Union-Find
    uf = UnionFind(num_vertices)
    mst = []
    
    for u, v, weight in edges:
        if not uf.is_same(u, v):
            uf.union(u, v)
            mst.append((u, v, weight))
            
            # MST has V-1 edges
            if len(mst) == num_vertices - 1:
                break
    
    return mst


def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """
    Check if graph is bipartite using BFS coloring.
    
    Args:
        graph: Adjacency list representation
        
    Returns:
        True if bipartite, False otherwise
        
    Time: O(V + E), Space: O(V)
    """
    color = {}
    
    def bfs_color(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            vertex = queue.popleft()
            
            for neighbor, _ in graph.get(vertex, []):
                if neighbor not in color:
                    color[neighbor] = 1 - color[vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:
                    return False
        
        return True
    
    vertices = set()
    for u in graph:
        vertices.add(u)
        for v, _ in graph[u]:
            vertices.add(v)
    
    for vertex in vertices:
        if vertex not in color:
            if not bfs_color(vertex):
                return False
    
    return True


def find_bridges(graph: Dict[int, List[int]]) -> List[Tuple[int, int]]:
    """
    Find all bridges (critical edges) in undirected graph using Tarjan's algorithm.
    
    Args:
        graph: Adjacency list representation of undirected graph
        
    Returns:
        List of bridge edges
        
    Time: O(V + E), Space: O(V)
    """
    visited = set()
    disc = {}  # Discovery time
    low = {}   # Low-link value
    parent = {}
    bridges = []
    time = [0]  # Use list to make it mutable in nested function
    
    def bridge_dfs(u):
        visited.add(u)
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v, _ in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                bridge_dfs(v)
                
                # Update low-link value
                low[u] = min(low[u], low[v])
                
                # Check if edge u-v is a bridge
                if low[v] > disc[u]:
                    bridges.append((u, v))
            
            elif v != parent.get(u):  # Back edge
                low[u] = min(low[u], disc[v])
    
    vertices = set()
    for u in graph:
        vertices.add(u)
        for v, _ in graph[u]:
            vertices.add(v)
    
    for vertex in vertices:
        if vertex not in visited:
            bridge_dfs(vertex)
    
    return bridges


def course_schedule(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if it's possible to finish all courses (cycle detection in DAG).
    
    Args:
        num_courses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        True if possible to finish all courses, False otherwise
        
    Time: O(V + E), Space: O(V + E)
    """
    # Build graph
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append((course, 1))
    
    # Check for cycle
    return not has_cycle_directed(graph)


def alien_dictionary(words: List[str]) -> str:
    """
    Find order of characters in alien language using topological sort.
    
    Args:
        words: List of words in alien language (sorted order)
        
    Returns:
        String representing character order, empty if invalid
        
    Time: O(C) where C is total characters, Space: O(1) for English alphabet
    """
    # Build graph of character dependencies
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    chars = set()
    
    # Initialize all characters
    for word in words:
        for char in word:
            chars.add(char)
            in_degree[char] = 0
    
    # Build edges based on adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        
        # Check if word1 is prefix of word2 but longer (invalid)
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
        
        # Find first different character
        for j in range(min_len):
            if word1[j] != word2[j]:
                graph[word1[j]].append((word2[j], 1))
                in_degree[word2[j]] += 1
                break
    
    # Topological sort
    queue = deque([char for char in chars if in_degree[char] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)
        
        for next_char, _ in graph[char]:
            in_degree[next_char] -= 1
            if in_degree[next_char] == 0:
                queue.append(next_char)
    
    return ''.join(result) if len(result) == len(chars) else ""


# Interview Tips and Common Patterns
"""
Graph Algorithms Interview Tips:

1. **Graph Representation**:
   - Adjacency List: Space efficient, good for sparse graphs
   - Adjacency Matrix: Good for dense graphs, O(1) edge lookup
   - Edge List: Simple representation, good for MST algorithms

2. **Traversal Algorithms**:
   - DFS: Use for cycle detection, topological sort, connected components
   - BFS: Use for shortest path (unweighted), level-order processing
   - Choose recursive vs iterative based on constraints

3. **Common Patterns**:
   - Cycle Detection: DFS with coloring (directed), DFS with parent tracking (undirected)
   - Shortest Path: BFS (unweighted), Dijkstra (weighted), Bellman-Ford (negative weights)
   - Topological Sort: Kahn's algorithm (BFS-based) or DFS-based
   - Connected Components: DFS or Union-Find

4. **Key Insights**:
   - Many problems reduce to graph traversal
   - Consider both directed and undirected cases
   - Watch for cycles in dependency problems
   - Use appropriate data structures (heap for Dijkstra, etc.)

5. **Python-Specific Tips**:
   - Use collections.defaultdict for adjacency lists
   - Use collections.deque for BFS queues
   - Leverage heapq for priority queues
   - Use sets for visited tracking

6. **Integration with Existing Code**:
   - Reuse Dijkstra implementation from Libs/
   - Leverage UnionFind for MST and connectivity
   - Extend existing implementations for interview problems

7. **Time/Space Complexity**:
   - DFS/BFS: O(V + E) time, O(V) space
   - Dijkstra: O((V + E) log V) time, O(V) space
   - Topological Sort: O(V + E) time, O(V) space
   - MST: O(E log E) time for Kruskal, O(V) space

8. **Common Applications**:
   - Course scheduling (topological sort)
   - Social networks (connected components)
   - Navigation systems (shortest path)
   - Network design (MST)
   - Dependency resolution (topological sort)
"""