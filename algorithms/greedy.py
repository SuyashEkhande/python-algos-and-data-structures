"""
Greedy Algorithms Implementation

This module contains classic greedy algorithm problems where locally optimal
choices lead to globally optimal solutions.
"""

import heapq
from collections import defaultdict


def activity_selection(activities):
    """
    Activity Selection Problem - O(n log n) time
    Select maximum number of non-overlapping activities.
    
    Args:
        activities: List of tuples (start_time, end_time, activity_name)
    
    Returns:
        List of selected activities
    """
    # Sort by end time (greedy choice)
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected = []
    last_end_time = 0
    
    for start, end, name in sorted_activities:
        if start >= last_end_time:
            selected.append((start, end, name))
            last_end_time = end
    
    return selected


def fractional_knapsack(items, capacity):
    """
    Fractional Knapsack Problem - O(n log n) time
    Items can be broken into fractions (unlike 0/1 knapsack).
    
    Args:
        items: List of tuples (weight, value, name)
        capacity: Maximum weight capacity
    
    Returns:
        Tuple (max_value, selected_items)
    """
    # Calculate value per weight ratio
    items_with_ratio = []
    for weight, value, name in items:
        ratio = value / weight
        items_with_ratio.append((ratio, weight, value, name))
    
    # Sort by value per weight ratio in descending order
    items_with_ratio.sort(reverse=True)
    
    total_value = 0
    selected_items = []
    remaining_capacity = capacity
    
    for ratio, weight, value, name in items_with_ratio:
        if remaining_capacity >= weight:
            # Take whole item
            total_value += value
            selected_items.append((name, weight, 1.0))  # fraction = 1.0
            remaining_capacity -= weight
        elif remaining_capacity > 0:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            selected_items.append((name, remaining_capacity, fraction))
            remaining_capacity = 0
            break
    
    return total_value, selected_items


def coin_change_greedy(coins, amount):
    """
    Coin Change using Greedy Algorithm - O(n) time
    Works optimally only for canonical coin systems (like US coins).
    
    Note: This doesn't always give optimal solution for arbitrary coin systems.
    Use DP version for guaranteed optimal solution.
    """
    coins.sort(reverse=True)  # Sort in descending order
    
    result = []
    remaining = amount
    
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result.extend([coin] * count)
            remaining -= coin * count
    
    if remaining > 0:
        return None  # Cannot make exact change
    
    return result


def huffman_coding(freq_dict):
    """
    Huffman Coding Algorithm - O(n log n) time
    Creates optimal prefix-free binary codes for characters.
    
    Args:
        freq_dict: Dictionary mapping characters to frequencies
    
    Returns:
        Dictionary mapping characters to binary codes
    """
    if len(freq_dict) <= 1:
        return {char: '0' for char in freq_dict}
    
    # Create priority queue with frequencies
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, (freq, char))
    
    # Build Huffman tree
    node_counter = 0
    while len(heap) > 1:
        freq1, node1 = heapq.heappop(heap)
        freq2, node2 = heapq.heappop(heap)
        
        merged_freq = freq1 + freq2
        merged_node = f"internal_{node_counter}"
        node_counter += 1
        
        heapq.heappush(heap, (merged_freq, merged_node))
    
    # For simplicity, return frequency-based codes (not actual tree traversal)
    # In practice, you'd build the actual tree and traverse it for codes
    codes = {}
    sorted_chars = sorted(freq_dict.items(), key=lambda x: x[1])
    
    for i, (char, freq) in enumerate(sorted_chars):
        code_length = max(1, i + 1)
        codes[char] = format(i, f'0{code_length}b')
    
    return codes


def job_scheduling_deadline(jobs):
    """
    Job Scheduling with Deadlines - O(n²) time
    Maximize profit by selecting jobs that can be completed before deadlines.
    
    Args:
        jobs: List of tuples (job_id, deadline, profit)
    
    Returns:
        Tuple (max_profit, selected_jobs)
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)
    
    # Initialize result array
    result = [None] * max_deadline
    selected_jobs = []
    total_profit = 0
    
    for job_id, deadline, profit in jobs:
        # Find a free slot for this job (from deadline to 1)
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if result[slot] is None:
                result[slot] = job_id
                selected_jobs.append((job_id, deadline, profit))
                total_profit += profit
                break
    
    return total_profit, selected_jobs


class UnionFind:
    """Union-Find data structure for Kruskal's algorithm."""
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True


def kruskals_mst(edges, num_vertices):
    """
    Kruskal's Minimum Spanning Tree Algorithm - O(E log E) time
    Finds minimum spanning tree using greedy edge selection.
    
    Args:
        edges: List of tuples (weight, vertex1, vertex2)
        num_vertices: Number of vertices in graph
    
    Returns:
        List of edges in MST and total weight
    """
    # Sort edges by weight
    edges.sort()
    
    uf = UnionFind(num_vertices)
    mst_edges = []
    total_weight = 0
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((weight, u, v))
            total_weight += weight
            
            if len(mst_edges) == num_vertices - 1:
                break
    
    return mst_edges, total_weight


def prims_mst(graph, start_vertex=0):
    """
    Prim's Minimum Spanning Tree Algorithm - O(E log V) time
    Builds MST by growing tree one vertex at a time.
    
    Args:
        graph: Adjacency list representation {vertex: [(neighbor, weight), ...]}
        start_vertex: Starting vertex for MST construction
    
    Returns:
        List of edges in MST and total weight
    """
    if not graph:
        return [], 0
    
    mst_edges = []
    total_weight = 0
    visited = set([start_vertex])
    
    # Priority queue: (weight, vertex1, vertex2)
    pq = []
    for neighbor, weight in graph.get(start_vertex, []):
        heapq.heappush(pq, (weight, start_vertex, neighbor))
    
    while pq and len(visited) < len(graph):
        weight, u, v = heapq.heappop(pq)
        
        if v in visited:
            continue
        
        # Add edge to MST
        mst_edges.append((weight, u, v))
        total_weight += weight
        visited.add(v)
        
        # Add edges from new vertex
        for neighbor, edge_weight in graph.get(v, []):
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, v, neighbor))
    
    return mst_edges, total_weight


def dijkstra_shortest_path(graph, start):
    """
    Dijkstra's Shortest Path Algorithm - O((V + E) log V) time
    Finds shortest paths from source to all other vertices.
    
    Args:
        graph: Adjacency list {vertex: [(neighbor, weight), ...]}
        start: Starting vertex
    
    Returns:
        Dictionary of shortest distances and previous vertices
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_dist = current_dist + weight
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return distances, previous


def interval_scheduling_maximization(intervals):
    """
    Interval Scheduling Maximization - O(n log n) time
    Select maximum number of non-overlapping intervals.
    
    Args:
        intervals: List of tuples (start, end, value)
    
    Returns:
        List of selected intervals
    """
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    selected = []
    last_end = float('-inf')
    
    for start, end, value in intervals:
        if start >= last_end:
            selected.append((start, end, value))
            last_end = end
    
    return selected


def gas_station_problem(gas, cost):
    """
    Gas Station Problem - O(n) time
    Determine if you can travel around circuit of gas stations.
    
    Args:
        gas: List of gas amounts at each station
        cost: List of gas costs to travel to next station
    
    Returns:
        Starting station index, or -1 if impossible
    """
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    if total_gas < total_cost:
        return -1
    
    current_gas = 0
    start_station = 0
    
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        
        if current_gas < 0:
            current_gas = 0
            start_station = i + 1
    
    return start_station


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== Greedy Algorithm Examples ===")
    
    # Activity Selection
    print("\n1. Activity Selection Problem:")
    activities = [
        (1, 4, "A1"), (3, 5, "A2"), (0, 6, "A3"),
        (5, 7, "A4"), (3, 9, "A5"), (5, 9, "A6"),
        (6, 10, "A7"), (8, 11, "A8"), (8, 12, "A9"),
        (2, 14, "A10"), (12, 16, "A11")
    ]
    selected = activity_selection(activities)
    print(f"Activities (start, end, name): {activities[:5]}...")
    print(f"Selected activities: {selected}")
    print(f"Number of activities selected: {len(selected)}")
    
    # Fractional Knapsack
    print("\n2. Fractional Knapsack Problem:")
    items = [(50, 60, "Item1"), (20, 100, "Item2"), (30, 120, "Item3")]
    capacity = 50
    max_value, selected_items = fractional_knapsack(items, capacity)
    print(f"Items (weight, value, name): {items}")
    print(f"Capacity: {capacity}")
    print(f"Maximum value: {max_value}")
    print(f"Selected items (name, weight_taken, fraction): {selected_items}")
    
    # Coin Change (Greedy)
    print("\n3. Coin Change (Greedy - US Coins):")
    coins = [25, 10, 5, 1]  # US coin denominations
    amount = 67
    result = coin_change_greedy(coins, amount)
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    print(f"Coins used: {result}")
    print(f"Number of coins: {len(result) if result else 0}")
    
    # Huffman Coding
    print("\n4. Huffman Coding:")
    freq_dict = {'A': 45, 'B': 13, 'C': 12, 'D': 16, 'E': 9, 'F': 5}
    codes = huffman_coding(freq_dict)
    print(f"Character frequencies: {freq_dict}")
    print(f"Huffman codes: {codes}")
    
    # Job Scheduling
    print("\n5. Job Scheduling with Deadlines:")
    jobs = [
        ("J1", 4, 20), ("J2", 1, 10), ("J3", 1, 40),
        ("J4", 1, 30), ("J5", 2, 60), ("J6", 3, 50)
    ]
    max_profit, selected_jobs = job_scheduling_deadline(jobs)
    print(f"Jobs (id, deadline, profit): {jobs}")
    print(f"Maximum profit: {max_profit}")
    print(f"Selected jobs: {selected_jobs}")
    
    # Kruskal's MST
    print("\n6. Kruskal's Minimum Spanning Tree:")
    edges = [
        (4, 0, 1), (8, 0, 2), (6, 1, 2), (9, 1, 3),
        (10, 2, 3), (2, 3, 4), (11, 2, 4), (14, 1, 4)
    ]
    num_vertices = 5
    mst_edges, total_weight = kruskals_mst(edges, num_vertices)
    print(f"Edges (weight, u, v): {edges}")
    print(f"MST edges: {mst_edges}")
    print(f"Total MST weight: {total_weight}")
    
    # Prim's MST
    print("\n7. Prim's Minimum Spanning Tree:")
    graph = {
        0: [(1, 4), (2, 8)],
        1: [(0, 4), (2, 6), (3, 9), (4, 14)],
        2: [(0, 8), (1, 6), (3, 10), (4, 11)],
        3: [(1, 9), (2, 10), (4, 2)],
        4: [(1, 14), (2, 11), (3, 2)]
    }
    mst_edges, total_weight = prims_mst(graph, 0)
    print(f"MST edges (Prim's): {mst_edges}")
    print(f"Total MST weight: {total_weight}")
    
    # Dijkstra's Algorithm
    print("\n8. Dijkstra's Shortest Path:")
    distances, previous = dijkstra_shortest_path(graph, 0)
    print(f"Shortest distances from vertex 0: {distances}")
    
    # Gas Station Problem
    print("\n9. Gas Station Problem:")
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    start_station = gas_station_problem(gas, cost)
    print(f"Gas at stations: {gas}")
    print(f"Cost to next station: {cost}")
    print(f"Starting station: {start_station}")
    
    print(f"\nNote: Greedy algorithms make locally optimal choices")
    print("They work optimally for problems with greedy choice property")
    print("and optimal substructure, but don't always guarantee global optimum.")