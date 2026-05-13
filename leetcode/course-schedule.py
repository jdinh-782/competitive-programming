# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. Initialize Graph and In-Degree array
        # graph[i] contains a list of all courses that require course i
        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph
        # Note the prompt formatting: [course, prereq] -> prereq must be taken first
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
            
        # 2. Find all courses with 0 prerequisites to start our queue
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        # 3. Process the queue (BFS)
        completed_courses = 0
        
        while queue:
            current = queue.popleft()
            completed_courses += 1
            
            # Decrease the in-degree of all dependent courses
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                
                # If a course now has 0 remaining prerequisites, we can take it!
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If we were able to complete all courses, there was no cycle

        # Complexity Analysis
        # Time Complexity O(V + E): Building the graph and populating the `in_degree` array requires iterating over the E prerequisites, taking O(E) time. Finding the initial 0-degree courses takes O(V) time. During the BFS traversal,
        #                           every valid node is popped from the queue exactly once, and every outgoing edge is traversed exactly once to decrement the neighbor's in-degree
        # Space Complexity O(V + E): Memory footprint is heavily dominated by the `graph` Adjacency List, which stores every directed edge, taking up to O(E) space. The `in_degree` tracking array and the `queue` each take strictly O(V)
        #                            space. Overall memory scales linearly with the size of the graph components
        return completed_courses == numCourses