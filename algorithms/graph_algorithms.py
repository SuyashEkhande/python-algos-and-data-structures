"""
Graph Algorithms Implementation

This module contains advanced graph algorithms including traversals,
shortest path algorithms, and network flow algorithms.
"""

from collections import deque, defaultdict
import heapq


def breadth_first_search_paths(graph, start, target):
    """
    BFS to find shortest path between start and target.
    Returns the path and distance.
    """
    if start == target:
        return [start], 0
    
    queue = deque([(start, [start], 0)])
    visited = {start}
    
    while queue:
        current, path, distance = queue.popleft()
        
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_distance = distance + weight
                
                if neighbor == target:
                    return new_path, new_distance
                
                visited.add(neighbor)
                queue.append((neighbor, new_path, new_distance))
    
    return None, float('inf')  # No path found


def depth_first_search_all_paths(graph, start, target, path=None):
    """
    DFS to find all paths between start and target.
    Returns list of all possible paths.
    """
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == target:
        return [path]
    
    paths = []
    for neighbor, weight in graph.get(start, []):
        if neighbor not in path:  # Avoid cycles
            new_paths = depth_first_search_all_paths(graph, neighbor, target, path)
            paths.extend(new_paths)
    
    return paths


def topological_sort_kahns(graph):
    """
    Topological Sort using Kahn's Algorithm (BFS approach).
    Works for Directed Acyclic Graphs (DAG).
    """
    # Calculate in-degrees
    in_degree = defaultdict(int)
    vertices = set()
    
    for vertex in graph:
        vertices.add(vertex)
        for neighbor, weight in graph[vertex]:
            vertices.add(neighbor)
            in_degree[neighbor] += 1
    
    # Initialize queue with vertices having 0 in-degree
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Reduce in-degree of neighbors
        for neighbor, weight in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if graph has cycle
    if len(result) != len(vertices):
        return None  # Graph has cycle
    
    return result


def detect_cycle_directed_dfs(graph):
    """
    Detect cycle in directed graph using DFS with color coding.
    Returns True if cycle exists, False otherwise.
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {vertex: WHITE for vertex in graph}
    
    def dfs_visit(vertex):
        color[vertex] = GRAY
        
        for neighbor, weight in graph.get(vertex, []):
            if color.get(neighbor, WHITE) == GRAY:
                return True  # Back edge found (cycle)
            elif color.get(neighbor, WHITE) == WHITE and dfs_visit(neighbor):
                return True
        
        color[vertex] = BLACK
        return False
    
    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs_visit(vertex):
                return True
    
    return False


def bellman_ford(graph, start):
    """
    Bellman-Ford Algorithm for shortest paths with negative weights.
    Can detect negative cycles.
    
    Returns: (distances, has_negative_cycle)
    """
    # Get all vertices
    vertices = set([start])
    for vertex in graph:
        vertices.add(vertex)
        for neighbor, weight in graph[vertex]:
            vertices.add(neighbor)
    
    # Initialize distances
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for vertex in graph:
            if distances[vertex] != float('inf'):
                for neighbor, weight in graph[vertex]:
                    if distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight
    
    # Check for negative cycles
    has_negative_cycle = False
    for vertex in graph:
        if distances[vertex] != float('inf'):
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    break
    
    return distances, has_negative_cycle


def floyd_warshall(graph):
    """
    Floyd-Warshall Algorithm for all-pairs shortest paths.
    Works with negative weights but not negative cycles.
    
    Returns: 2D distance matrix
    """
    # Get all vertices
    vertices = set()
    for vertex in graph:
        vertices.add(vertex)
        for neighbor, weight in graph[vertex]:
            vertices.add(neighbor)
    
    vertices = sorted(list(vertices))
    n = len(vertices)
    vertex_to_index = {v: i for i, v in enumerate(vertices)}
    
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance from vertex to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Fill direct edges
    for vertex in graph:
        i = vertex_to_index[vertex]
        for neighbor, weight in graph[vertex]:
            j = vertex_to_index[neighbor]
            dist[i][j] = weight
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist, vertices


def strongly_connected_components(graph):
    """
    Find Strongly Connected Components using Kosaraju's Algorithm.
    
    Returns: List of SCCs, where each SCC is a list of vertices
    """
    # Step 1: Perform DFS on original graph to get finish times
    visited = set()
    finish_order = []
    
    def dfs1(vertex):
        visited.add(vertex)
        for neighbor, weight in graph.get(vertex, []):
            if neighbor not in visited:
                dfs1(neighbor)
        finish_order.append(vertex)
    
    for vertex in graph:
        if vertex not in visited:
            dfs1(vertex)
    
    # Step 2: Create transpose graph
    transpose = defaultdict(list)
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            transpose[neighbor].append((vertex, weight))
    
    # Step 3: DFS on transpose in reverse finish order
    visited = set()
    sccs = []
    
    def dfs2(vertex, current_scc):
        visited.add(vertex)
        current_scc.append(vertex)
        for neighbor, weight in transpose.get(vertex, []):
            if neighbor not in visited:
                dfs2(neighbor, current_scc)
    
    for vertex in reversed(finish_order):
        if vertex not in visited:
            current_scc = []
            dfs2(vertex, current_scc)
            sccs.append(current_scc)
    
    return sccs


def articulation_points(graph):
    """
    Find articulation points (cut vertices) using Tarjan's algorithm.
    Articulation points are vertices whose removal increases connected components.
    """
    visited = set()
    discovery = {}
    low = {}
    parent = {}
    articulation_points = set()
    time = [0]  # Use list to modify in nested function
    
    def dfs(vertex):
        children = 0
        visited.add(vertex)
        discovery[vertex] = low[vertex] = time[0]
        time[0] += 1
        
        for neighbor, weight in graph.get(vertex, []):
            if neighbor not in visited:
                children += 1
                parent[neighbor] = vertex
                dfs(neighbor)
                
                # Update low value
                low[vertex] = min(low[vertex], low[neighbor])
                
                # Check articulation point conditions
                if parent.get(vertex) is None and children > 1:
                    # Root with more than one child
                    articulation_points.add(vertex)
                elif parent.get(vertex) is not None and low[neighbor] >= discovery[vertex]:
                    # Non-root vertex
                    articulation_points.add(vertex)
            
            elif neighbor != parent.get(vertex):
                # Back edge
                low[vertex] = min(low[vertex], discovery[neighbor])
    
    for vertex in graph:
        if vertex not in visited:
            parent[vertex] = None
            dfs(vertex)
    
    return list(articulation_points)


def bridges(graph):
    """
    Find bridges (cut edges) using Tarjan's algorithm.
    Bridges are edges whose removal increases connected components.
    """
    visited = set()
    discovery = {}
    low = {}
    parent = {}
    bridges_list = []
    time = [0]
    
    def dfs(vertex):
        visited.add(vertex)
        discovery[vertex] = low[vertex] = time[0]
        time[0] += 1
        
        for neighbor, weight in graph.get(vertex, []):
            if neighbor not in visited:
                parent[neighbor] = vertex
                dfs(neighbor)
                
                low[vertex] = min(low[vertex], low[neighbor])
                
                # Check if edge is a bridge
                if low[neighbor] > discovery[vertex]:
                    bridges_list.append((vertex, neighbor))
            
            elif neighbor != parent.get(vertex):
                low[vertex] = min(low[vertex], discovery[neighbor])
    
    for vertex in graph:
        if vertex not in visited:
            parent[vertex] = None
            dfs(vertex)
    
    return bridges_list


def is_bipartite_coloring(graph):
    """
    Check if graph is bipartite using 2-coloring.
    Returns True if bipartite, False otherwise.
    Also returns the coloring if bipartite.
    """
    color = {}
    
    def bfs_color(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            vertex = queue.popleft()
            
            for neighbor, weight in graph.get(vertex, []):
                if neighbor not in color:
                    color[neighbor] = 1 - color[vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:
                    return False
        
        return True
    
    for vertex in graph:
        if vertex not in color:
            if not bfs_color(vertex):
                return False, None
    
    return True, color


def hamiltonian_path_backtrack(graph, start=None):
    """
    Find Hamiltonian path using backtracking.
    Returns path if exists, None otherwise.
    """
    vertices = list(graph.keys())
    if start is None:
        start = vertices[0]
    
    n = len(vertices)
    path = [start]
    visited = {start}
    
    def backtrack():
        if len(path) == n:
            return True
        
        current = path[-1]
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                path.append(neighbor)
                visited.add(neighbor)
                
                if backtrack():
                    return True
                
                path.pop()
                visited.remove(neighbor)
        
        return False
    
    if backtrack():
        return path
    return None


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== Advanced Graph Algorithms ===")
    
    # Test graph for demonstrations
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    print(f"Test graph: {graph}")
    
    # BFS shortest path
    print("\n1. BFS Shortest Path:")
    path, distance = breadth_first_search_paths(graph, 'A', 'D')
    print(f"Shortest path from A to D: {path} (distance: {distance})")
    
    # DFS all paths
    print("\n2. DFS All Paths:")
    all_paths = depth_first_search_all_paths(graph, 'A', 'D')
    print(f"All paths from A to D: {all_paths}")
    
    # Directed graph for cycle detection and topological sort
    directed_graph = {
        'A': [('B', 1), ('C', 1)],
        'B': [('D', 1)],
        'C': [('D', 1)],
        'D': []
    }
    
    print(f"\n3. Directed Graph: {directed_graph}")
    
    # Topological sort
    topo_order = topological_sort_kahns(directed_graph)
    print(f"Topological order: {topo_order}")
    
    # Cycle detection
    has_cycle = detect_cycle_directed_dfs(directed_graph)
    print(f"Has cycle: {has_cycle}")
    
    # Graph with negative weights for Bellman-Ford
    negative_graph = {
        'A': [('B', -1), ('C', 4)],
        'B': [('C', 3), ('D', 2)],
        'C': [],
        'D': [('B', 1)]
    }
    
    print(f"\n4. Bellman-Ford (with negative weights):")
    print(f"Graph: {negative_graph}")
    distances, has_neg_cycle = bellman_ford(negative_graph, 'A')
    print(f"Distances from A: {distances}")
    print(f"Has negative cycle: {has_neg_cycle}")
    
    # Floyd-Warshall
    print(f"\n5. Floyd-Warshall (All-pairs shortest paths):")
    dist_matrix, vertices = floyd_warshall(graph)
    print(f"Vertices: {vertices}")
    print("Distance matrix:")
    for i, row in enumerate(dist_matrix):
        print(f"  {vertices[i]}: {row}")
    
    # Strongly Connected Components
    scc_graph = {
        'A': [('B', 1)],
        'B': [('C', 1)],
        'C': [('A', 1), ('D', 1)],
        'D': [('E', 1)],
        'E': [('F', 1)],
        'F': [('D', 1)]
    }
    
    print(f"\n6. Strongly Connected Components:")
    print(f"Graph: {scc_graph}")
    sccs = strongly_connected_components(scc_graph)
    print(f"SCCs: {sccs}")
    
    # Articulation points and bridges
    bridge_graph = {
        'A': [('B', 1), ('C', 1)],
        'B': [('A', 1), ('C', 1), ('D', 1)],
        'C': [('A', 1), ('B', 1)],
        'D': [('B', 1), ('E', 1)],
        'E': [('D', 1)]
    }
    
    print(f"\n7. Articulation Points and Bridges:")
    print(f"Graph: {bridge_graph}")
    art_points = articulation_points(bridge_graph)
    bridge_list = bridges(bridge_graph)
    print(f"Articulation points: {art_points}")
    print(f"Bridges: {bridge_list}")
    
    # Bipartite check
    print(f"\n8. Bipartite Graph Check:")
    is_bip, coloring = is_bipartite_coloring(graph)
    print(f"Is bipartite: {is_bip}")
    if coloring:
        print(f"2-coloring: {coloring}")
    
    # Hamiltonian path
    print(f"\n9. Hamiltonian Path:")
    ham_path = hamiltonian_path_backtrack(graph, 'A')
    print(f"Hamiltonian path starting from A: {ham_path}")
    
    print(f"\nNote: These algorithms solve various graph problems:")
    print("- Connectivity: SCCs, articulation points, bridges")
    print("- Shortest paths: Dijkstra, Bellman-Ford, Floyd-Warshall") 
    print("- Traversals: BFS, DFS with various applications")
    print("- Special properties: bipartite, Hamiltonian, topological ordering")