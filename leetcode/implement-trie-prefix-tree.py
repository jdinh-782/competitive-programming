# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class TrieNode:
    def __init__(self):
        # Hash map for O(1) child lookups
        self.children = {}
        # Marks the end of a valid inserted word
        self.is_end = False

class Trie:
    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the character path doesn't exist, create it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move down the tree
            curr = curr.children[char]
        
        # Mark the final node as the end of the word
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # If a character is missing, the word doesn't exist
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # We found the path, but we must verify it's a complete word
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # If we successfully traversed the prefix, it exists
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)