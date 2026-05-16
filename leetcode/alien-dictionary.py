# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # 1. Initialize Adjacency List for all UNIQUE characters in the dictionary
        # It's critical to initialize even isolated characters that have no edges.
        adj = {c: set() for w in words for c in w}
        
        # 2. Build the Graph (Extract the rules)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Edge Case: If w1 is a longer prefix of w2, the order is invalid.
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
                
            # Find the first differing character to establish a directed edge
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break # Critical: Only the first difference defines order
                    
        # 3. Topological Sort (DFS with 3-State Cycle Detection)
        visited = {} # False = Visiting (in current path), True = Visited (fully processed)
        res = []
        
        def dfs(char: str) -> bool:
            # If the char is already in our tracker, return True if it's fully processed,
            # or False if it's currently 'Visiting' (which means we detected a cycle!)
            if char in visited:
                return visited[char]
                
            # Mark as 'Visiting' (in the current recursive path)
            visited[char] = False
            
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False # Cycle detected deep in the recursion
                    
            # Mark as 'Visited' (fully processed) and append to Post-Order result
            visited[char] = True
            res.append(char)
            return True
            
        # 4. Execute DFS for every unique character in the graph
        for char in adj:
            if not dfs(char):
                return "" # Cycle detected, invalid dictionary
                
        # 5. Reverse the post-order traversal to get the valid Topological Sort
        res.reverse()

        # Complexity Analysis
        # Time Complexity O(N): Extracting the rules requires iterating through adjacent words and comparing their characters. In the worst case, we evaluate every single character in the input, taking O(N) time. DFS traversal takes O(V + E),
        #                       where V <= 26 and edges E <= 26^2. Since V and E are strictly bounded constants, the DFS executes in O(1) time. Therefore, the dominant operation is reading the input, yielding a strictly linear O(N) time complexity
        # Space Complexity O(1): The memory footprint is dictated entirely by our Adjacency List, the 3-state visited tracker, and the recursion Call Stack. Because the alphabet is capped at 26 unique characters, the graph will have a maximum of 
        #                        26 nodes and 26^2 edges. Memory scales at a strict, unbreakable constant upper bound of O(1)
        return "".join(res)