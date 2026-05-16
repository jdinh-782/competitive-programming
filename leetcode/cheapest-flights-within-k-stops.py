# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # 1. Initialize prices to infinity, except the source node
        prices = [float('inf')] * n
        prices[src] = 0
        
        # 2. Run exactly K + 1 iterations (K stops means K + 1 edges max)
        for i in range(k + 1):
            # Create a temporary copy to prevent multi-edge chaining in a single iteration
            tmp_prices = prices.copy()
            
            # 3. Process every flight (edge relaxation)
            for u, v, p in flights:
                # If the source city 'u' has been reached in previous iterations
                if prices[u] == float('inf'):
                    continue
                    
                # If the new price is cheaper, update the TEMPORARY array
                if prices[u] + p < tmp_prices[v]:
                    tmp_prices[v] = prices[u] + p
            
            # 4. Commit the temporary array for the next wave
            prices = tmp_prices
            
        # 5. Final check

        # Complexity Analysis
        # Time Complexity O(K x E): The algorithm strictly runs an outer loop exactly K + 1 times. Inside that loop, it blindly iterates over all E flights to perform edge relaxation. Therefore, the processing time is highly predictable 
        #                           and scales strictly by multiplying the number of allowed iterations by the total number of edges
        # Space Complexity O(V): By utilizing Bellman-Ford, I entirely bypass the need to build a heavy Graph Adjacency List. The memory footprint is perfectly flat, dictated entirely by the `prices` and `tmp_prices` tracking arrays of size V
        return prices[dst] if prices[dst] != float('inf') else -1