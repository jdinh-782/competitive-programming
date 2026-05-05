# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n == 0:
            return len(tasks)
            
        # 1. Get the frequencies of all tasks
        counts = Counter(tasks)
        
        # 2. Find the maximum frequency among all tasks
        max_freq = max(counts.values())
        
        # 3. Count how many tasks tie for that maximum frequency
        tasks_with_max_freq = sum(1 for count in counts.values() if count == max_freq)
        
        # 4. Calculate the required intervals based on the chunking formula
        # (max_freq - 1) gives us the number of full chunks.
        # (n + 1) is the length of each chunk (1 slot for the task, n slots for cooldown).
        # We add tasks_with_max_freq for the tasks sitting at the very tail end.
        calculated_intervals = (max_freq - 1) * (n + 1) + tasks_with_max_freq
        
        # 5. Return the maximum of the calculated intervals or the raw number of tasks.
        # If the raw list is longer, it means we had zero idle time!

        # Complexity Analysis
        # Time Complexity O(T): Iterate through the `tasks` array exactly once to build our `Counter` hash
        #                       map, which takes O(T) time. Finding the max frequency and summing the ties
        #                       iterates over the values of the hash map
        # Space Complexity O(1): Hash map stores the frequencies of the tasks. Given the constraint of 26 possible
        #                        unique task names, the size of our hash map is mathematically bounded to a max
        #                        of 26 keys. Therefore, the memory footprint is strictly O(1) constant space
        return max(len(tasks), calculated_intervals)