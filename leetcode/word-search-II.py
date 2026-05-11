# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # Store the full word here instead of a boolean

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word # Mark the end of the word
            
        ROWS, COLS = len(board), len(board[0])
        res = []
        
        # 2. Define the Trie-guided DFS
        def dfs(r: int, c: int, node: TrieNode):
            # If we reached a node that contains a word, we found a match!
            if node.word:
                res.append(node.word)
                node.word = None # OPTIMIZATION: Remove word to prevent duplicates/redundant work
                
            # Boundary & Visited Checks
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] not in node.children):
                return
            
            char = board[r][c]
            curr_node = node.children[char]
            
            # Mark cell as visited by mutating it
            board[r][c] = "#"
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c, curr_node)
            dfs(r - 1, c, curr_node)
            dfs(r, c + 1, curr_node)
            dfs(r, c - 1, curr_node)
            
            # Backtrack: Restore the cell
            board[r][c] = char
            
            # OPTIMIZATION: Prune empty Trie nodes to speed up future DFS paths
            if not curr_node.children:
                del node.children[char]

        # 3. Kick off DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return res