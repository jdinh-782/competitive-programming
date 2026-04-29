# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map key -> Node
        
        # Dummy head and tail to avoid edge cases during insertion/deletion
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- Helper Functions for the Doubly Linked List ---
    def _remove(self, node: Node):
        """Remove an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        """Insert a node right after the dummy head (Most Recently Used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # --- Main LRU Logic ---
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to Most Recently Used position
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to MRU position
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._add_to_front(node)
        else:
            # Create new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Evict the LRU node (the one right before the dummy tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]