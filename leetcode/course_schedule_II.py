# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 1. Initialize Graph and In-Degree array
        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph
        # [course, prereq] -> prereq must be taken first
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
            
        # 2. Find all courses with 0 prerequisites to seed the queue
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        # 3. Process the queue to build the Topological Sort
        order = []
        
        while queue:
            current = queue.popleft()
            order.append(current) # Record the execution order
            
            # Decrease the in-degree of all dependent courses
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                
                # If a course has 0 remaining prerequisites, it's ready!
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If the order length matches numCourses, return it. Otherwise, return [] (cycle)
        if len(order) == numCourses:
            return order

        # Complexity Analysis
        # Time Complexity O(V + E): Building the graph and the `in_degree` array requires iterating over the E prerequisites exactly once. Scanning for the initial 0-degree courses takes O(V) time. During the BFS traversal,
        #                           every valid node is popped from the queue exactly once, and every outgoing edge is traversed exactly once to decrement a neighbor's in-degree
        # Space Complexity O(V + E): Memory footprint is dominated by the `graph` Adjacency List, which stores every directed edge, taking up to O(E) space. The `in_degree` tracking array, the `queue`, and the returned `order` array
        #                            each take strictly O(V) space
        return []