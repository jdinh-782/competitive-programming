# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Edge case: If endWord isn't in the list, no transformation is possible
        if endWord not in wordList:
            return 0
        
        # 1. Build the Adjacency List using Wildcard Patterns
        # e.g., nei["*ot"] = ["hot", "dot", "lot"]
        nei = collections.defaultdict(list)
        wordList.append(beginWord) # Ensure beginWord is in the processing pool
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
                
        # 2. Initialize BFS Queue and Visited Set
        visit = set([beginWord])
        queue = collections.deque([(beginWord, 1)]) # (word, level)
        
        # 3. BFS Traversal
        while queue:
            current_word, level = queue.popleft()
            
            # Base Case: Found the target word!
            if current_word == endWord:
                return level
            
            # Generate patterns for the current word to find neighbors
            for j in range(len(current_word)):
                pattern = current_word[:j] + "*" + current_word[j+1:]
                
                # Check all valid neighbors sharing this pattern
                for neighbor in nei[pattern]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append((neighbor, level + 1))
        
        # Complexity Analysis
        # Time Complexity O(N * M^2): For each of the N words, we iterate M times to replace a character with a wildcard. In Python, string slicing
        #                             requires allocating a new string, taking O(M) time
        # Space Complexity O(N * M^2): Memory footprint is dictated by the `nei` hash map. Every word of length M is stored M times across
        #                              different wildcard pattern keys. Storing N words M times yields an O(N * M^2) space complexity. Spatial cost
        #                              of the `queue` and `visited` set is O(N)
        return 0