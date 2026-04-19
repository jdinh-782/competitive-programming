# Name: Johnson Dinh
# Time: 16:38
# Language: Python3
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Checking if s1 is longer than s2 is a base case since s1 cannot be a permutation of s2 if it has more characters than s2
        if len(s1) > len(s2):
            return False

        # Iterate through s2 and check if any substring of s2 with the same length as s1 is a permutation of s1 by sorting both strings and comparing them
        begin = 0
        limit = len(s1)
        s1_sorted = sorted(s1)

        while begin < len(s2):
            p = s2[begin:limit]

            # Sort the substring and compare it to the sorted s1 to check if they are permutations of each other
            if s1_sorted == sorted(p):
                return True

            begin += 1
            limit += 1
        
        # Complexity Analysis
        # Time Complexity O(N * M log M): We iterate through s2 (N) and for each substring of length M (length of s1), we sort it which takes O(M log M)
        # Space Complexity O(M): Sorting the substring and s1 both require O(M) space where M is the length of s1
        return False


    def checkInclusionOptimized(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Initialize frequency arrays of size 26 for 'a' through 'z'
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Populate the initial frequencies for the first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # Check if the very first window is a match
        if s1_count == window_count:
            return True
            
        # Slide the window across the rest of s2
        for i in range(len(s1), len(s2)):
            # Add the new character entering the window on the right
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Remove the old character falling out of the window on the left
            left_char_index = i - len(s1)
            window_count[ord(s2[left_char_index]) - ord('a')] -= 1
            
            # Compare the arrays (takes O(1) time because size is fixed at 26)
            if s1_count == window_count:
                return True
    
        # Complexity Analysis
        # Time Complexity O(N): We iterate through s2 once (N) and comparing the frequency arrays takes O(1) time since they are of fixed size (26)
        # Space Complexity O(1): The frequency arrays are of fixed size (26) regardless of input size
        return False