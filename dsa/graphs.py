"""
Graph Data Structure Implementation

This module contains graph implementations using adjacency list and adjacency matrix,
along with common graph algorithms like BFS, DFS, and shortest path algorithms.
"""

from collections import deque, defaultdict
import heapq


class Graph:
    """Graph implementation using adjacency list."""
    
    def __init__(self, directed=False):
        self.directed = directed
        self.vertices = {}
        self.vertex_count = 0
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.vertices:
            self.vertices[vertex] = []
            self.vertex_count += 1
    
    def add_edge(self, v1, v2, weight=1):
        """Add an edge between two vertices."""
        # Ensure both vertices exist
        self.add_vertex(v1)
        self.add_vertex(v2)
        
        # Add edge
        self.vertices[v1].append((v2, weight))
        
        # If undirected, add reverse edge
        if not self.directed:
            self.vertices[v2].append((v1, weight))
    
    def get_vertices(self):
        """Return all vertices in the graph."""
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex."""
        return self.vertices.get(vertex, [])
    
    def has_edge(self, v1, v2):
        """Check if edge exists between two vertices."""
        if v1 not in self.vertices:
            return False
        
        neighbors = [neighbor for neighbor, weight in self.vertices[v1]]
        return v2 in neighbors
    
    def bfs(self, start_vertex):
        """Breadth-First Search traversal."""
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        queue = deque([start_vertex])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add unvisited neighbors to queue
                for neighbor, weight in self.vertices[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs(self, start_vertex):
        """Depth-First Search traversal (iterative)."""
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        stack = [start_vertex]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add unvisited neighbors to stack
                for neighbor, weight in self.vertices[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start_vertex, visited=None):
        """Depth-First Search traversal (recursive)."""
        if visited is None:
            visited = set()
        
        if start_vertex not in self.vertices or start_vertex in visited:
            return []
        
        visited.add(start_vertex)
        result = [start_vertex]
        
        for neighbor, weight in self.vertices[start_vertex]:
            result.extend(self.dfs_recursive(neighbor, visited))
        
        return result
    
    def has_cycle(self):
        """Detect cycle in graph using DFS."""
        if self.directed:
            return self._has_cycle_directed()
        else:
            return self._has_cycle_undirected()
    
    def _has_cycle_directed(self):
        """Detect cycle in directed graph."""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {vertex: WHITE for vertex in self.vertices}
        
        def dfs_visit(vertex):
            color[vertex] = GRAY
            
            for neighbor, weight in self.vertices[vertex]:
                if color[neighbor] == GRAY:  # Back edge found
                    return True
                elif color[neighbor] == WHITE and dfs_visit(neighbor):
                    return True
            
            color[vertex] = BLACK
            return False
        
        for vertex in self.vertices:
            if color[vertex] == WHITE:
                if dfs_visit(vertex):
                    return True
        
        return False
    
    def _has_cycle_undirected(self):
        """Detect cycle in undirected graph."""
        visited = set()
        
        def dfs_visit(vertex, parent):
            visited.add(vertex)
            
            for neighbor, weight in self.vertices[vertex]:
                if neighbor not in visited:
                    if dfs_visit(neighbor, vertex):
                        return True
                elif neighbor != parent:  # Back edge found
                    return True
            
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if dfs_visit(vertex, None):
                    return True
        
        return False
    
    def topological_sort(self):
        """Topological sort for directed acyclic graph."""
        if not self.directed:
            raise ValueError("Topological sort only applies to directed graphs")
        
        visited = set()
        stack = []
        
        def dfs_visit(vertex):
            visited.add(vertex)
            
            for neighbor, weight in self.vertices[vertex]:
                if neighbor not in visited:
                    dfs_visit(neighbor)
            
            stack.append(vertex)
        
        for vertex in self.vertices:
            if vertex not in visited:
                dfs_visit(vertex)
        
        return stack[::-1]  # Reverse to get topological order
    
    def dijkstra(self, start_vertex):
        """Dijkstra's shortest path algorithm."""
        if start_vertex not in self.vertices:
            return {}
        
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        # Priority queue: (distance, vertex)
        pq = [(0, start_vertex)]
        visited = set()
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.vertices[current_vertex]:
                if neighbor not in visited:
                    new_distance = current_distance + weight
                    
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_vertex
                        heapq.heappush(pq, (new_distance, neighbor))
        
        return distances, previous
    
    def get_shortest_path(self, start, end):
        """Get shortest path between two vertices using Dijkstra."""
        distances, previous = self.dijkstra(start)
        
        if distances[end] == float('inf'):
            return None  # No path exists
        
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        return path[::-1], distances[end]
    
    def __str__(self):
        result = []
        for vertex in self.vertices:
            neighbors = [f"{neighbor}({weight})" for neighbor, weight in self.vertices[vertex]]
            result.append(f"{vertex}: {neighbors}")
        return "\n".join(result)


class GraphMatrix:
    """Graph implementation using adjacency matrix."""
    
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertex_map = {}  # Map vertex names to indices
        self.reverse_map = {}  # Map indices to vertex names
        self.vertex_count = 0
    
    def add_vertex(self, vertex):
        """Add a vertex (assign it an index)."""
        if vertex not in self.vertex_map and self.vertex_count < self.num_vertices:
            self.vertex_map[vertex] = self.vertex_count
            self.reverse_map[self.vertex_count] = vertex
            self.vertex_count += 1
            return True
        return False
    
    def add_edge(self, v1, v2, weight=1):
        """Add an edge between two vertices."""
        if v1 not in self.vertex_map:
            self.add_vertex(v1)
        if v2 not in self.vertex_map:
            self.add_vertex(v2)
        
        if v1 in self.vertex_map and v2 in self.vertex_map:
            i, j = self.vertex_map[v1], self.vertex_map[v2]
            self.matrix[i][j] = weight
            
            if not self.directed:
                self.matrix[j][i] = weight
    
    def has_edge(self, v1, v2):
        """Check if edge exists between two vertices."""
        if v1 in self.vertex_map and v2 in self.vertex_map:
            i, j = self.vertex_map[v1], self.vertex_map[v2]
            return self.matrix[i][j] != 0
        return False
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex."""
        if vertex not in self.vertex_map:
            return []
        
        i = self.vertex_map[vertex]
        neighbors = []
        
        for j in range(self.num_vertices):
            if self.matrix[i][j] != 0:
                neighbors.append((self.reverse_map[j], self.matrix[i][j]))
        
        return neighbors
    
    def display(self):
        """Display the adjacency matrix."""
        print("Adjacency Matrix:")
        print("   ", end="")
        for i in range(self.vertex_count):
            print(f"{self.reverse_map[i]:>3}", end="")
        print()
        
        for i in range(self.vertex_count):
            print(f"{self.reverse_map[i]:>3}", end="")
            for j in range(self.vertex_count):
                print(f"{self.matrix[i][j]:>3}", end="")
            print()


def is_bipartite(graph, start_vertex):
    """
    Check if graph is bipartite using BFS.
    Returns True if bipartite, False otherwise.
    """
    color = {}
    queue = deque([start_vertex])
    color[start_vertex] = 0
    
    while queue:
        vertex = queue.popleft()
        
        for neighbor, weight in graph.get_neighbors(vertex):
            if neighbor not in color:
                color[neighbor] = 1 - color[vertex]
                queue.append(neighbor)
            elif color[neighbor] == color[vertex]:
                return False
    
    return True


def find_connected_components(graph):
    """
    Find all connected components in undirected graph.
    Returns list of components, where each component is a list of vertices.
    """
    visited = set()
    components = []
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            component = []
            stack = [vertex]
            
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    
                    for neighbor, weight in graph.get_neighbors(current):
                        if neighbor not in visited:
                            stack.append(neighbor)
            
            components.append(component)
    
    return components


# Example usage and demonstrations
if __name__ == "__main__":
    # Graph with adjacency list example
    print("=== Graph (Adjacency List) Example ===")
    g = Graph()
    
    # Add edges
    edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), ('B', 'D', 5), ('C', 'D', 1)]
    for v1, v2, weight in edges:
        g.add_edge(v1, v2, weight)
    
    print("Graph structure:")
    print(g)
    
    print(f"\nBFS from A: {g.bfs('A')}")
    print(f"DFS from A: {g.dfs('A')}")
    print(f"DFS recursive from A: {g.dfs_recursive('A')}")
    
    # Shortest path example
    distances, previous = g.dijkstra('A')
    print(f"\nShortest distances from A: {distances}")
    
    path, distance = g.get_shortest_path('A', 'D')
    print(f"Shortest path from A to D: {path} (distance: {distance})")
    
    # Cycle detection
    print(f"Has cycle: {g.has_cycle()}")
    
    # Directed graph example
    print("\n=== Directed Graph Example ===")
    dg = Graph(directed=True)
    directed_edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')]
    for v1, v2 in directed_edges:
        dg.add_edge(v1, v2)
    
    print(f"Directed graph has cycle: {dg.has_cycle()}")
    
    # Topological sort example
    dag = Graph(directed=True)
    dag_edges = [('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')]
    for v1, v2 in dag_edges:
        dag.add_edge(v1, v2)
    
    print(f"Topological sort: {dag.topological_sort()}")
    
    # Graph matrix example
    print("\n=== Graph (Adjacency Matrix) Example ===")
    gm = GraphMatrix(4)
    gm.add_vertex('X')
    gm.add_vertex('Y')
    gm.add_vertex('Z')
    gm.add_vertex('W')
    
    gm.add_edge('X', 'Y', 1)
    gm.add_edge('Y', 'Z', 2)
    gm.add_edge('Z', 'W', 3)
    gm.add_edge('W', 'X', 4)
    
    gm.display()
    
    # Connected components example
    print("\n=== Connected Components Example ===")
    ug = Graph()
    # Create disconnected graph
    ug.add_edge('A', 'B')
    ug.add_edge('B', 'C')
    ug.add_edge('D', 'E')
    ug.add_vertex('F')  # Isolated vertex
    
    components = find_connected_components(ug)
    print(f"Connected components: {components}")
    
    # Bipartite check example
    print(f"\nIs graph bipartite: {is_bipartite(g, 'A')}")