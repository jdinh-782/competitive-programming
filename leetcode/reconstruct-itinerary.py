# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import collections

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # 1. Build the Adjacency List
        adj = collections.defaultdict(list)
        
        # We sort tickets in reverse order before appending.
        # This ensures that for any given origin, its destinations are sorted
        # in reverse lexicographical order (e.g., ['SFO', 'ATL']).
        # This allows us to use .pop() to get the smallest lexical destination in O(1) time.
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        itinerary = []
        
        # 2. Post-Order DFS (Hierholzer's Algorithm)
        def dfs(airport: str):
            # While the current airport still has outgoing flights
            while adj[airport]:
                # Pop the smallest lexical destination and recursively visit it
                next_dest = adj[airport].pop()
                dfs(next_dest)
            
            # When we are completely stuck (no outgoing flights), 
            # we append the current airport to our itinerary.
            itinerary.append(airport)
            
        # 3. Trigger the traversal from JFK
        dfs("JFK")
        
        # 4. Reverse the post-order result to get the chronological path

        # Complexity Analysis
        # Time Complexity O(E log E): Sorting the list of tickets initially takes O(E log E) time. Building the graph takes O(E). During the actual DFS traversal, every ticket is popped
        #                             and traversed exactly once. Because of reverse-sort optimization, popping takes O(1) time per edge, meaning the DFS itself runs in strictly O(E)
        #                             time. Overall time complexity is heavily dominated by the initial sorting phase
        # Space Complexity O(V + E): The `adj` Hash Map stores every airport as a key and every ticket as a value, taking O(V + E) space. The recursive Call Stack and the returned
        #                            `itinerary` array will both hold exactly E + 1 elements in the worst case, taking O(E) space. Overall space scales linearly with the graph size
        return itinerary[::-1]