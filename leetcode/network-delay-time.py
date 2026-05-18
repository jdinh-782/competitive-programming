# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 1. Build the Adjacency List
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Min-heap stores: (accumulated_time, node)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0
        
        # 2. Execute Dijkstra's Algorithm
        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)
            
            # If we already locked in the shortest path to this node, skip it
            if current_node in visited:
                continue
                
            # 3. Lock in the node and record the time
            visited.add(current_node)
            max_time = max(max_time, current_time)
            
            # Early exit: if all nodes are reached, we can stop
            if len(visited) == n:
                return max_time
                
            # 4. Expand the frontier to all neighbors
            for neighbor, travel_time in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (current_time + travel_time, neighbor))
                    
        # 5. If we exit the loop and haven't visited all nodes, some are unreachable

        # Complexity Analysis
        # Time Complexity O(E log V): Building the graph takes O(E) time. During traversal, we could potentially push every single edge onto the Min-Heap in the worst-case scenario. The heap
        #                             can grow to size E. Pushing and popping from a heap of size E takes log(E) time. Because a simple graph can have at most V^2 edges (E <= V^2), log(E) is
        #                             mathematically bounded by log(V^2), which simplifies to 2log(V). Therefore, the time complexity scales strictly to O(E log V)
        # Space Complexity O(V + E): The `graph` adjacency list will store all V nodes and E edges. The `visited` set stores up to V nodes. Finally, the `min_heap` can hold up to O(E) elements
        #                            simultaneously in a highly branched graph. The overall memory footprint scales linearly with the network size
        return -1