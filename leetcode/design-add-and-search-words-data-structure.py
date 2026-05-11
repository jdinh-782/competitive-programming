# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        
        # Nested DFS helper to handle the wildcard branching
        def dfs(index: int, root: TrieNode) -> bool:
            curr = root
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == ".":
                    # Wildcard: Branch out and check ALL children
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    # If all branches fail, this path is a dead end
                    return False
                else:
                    # Standard Trie lookup
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                    
            return curr.is_end
        
        # Kick off DFS from the root at index 0
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)