# Name: Johnson Dinh
# Time: 15:14
# Language: Python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base case is to return length of string since longest substring without repeating characters is the string itself if there are no duplicates
        if len(s) < 2:
            return len(s)
        
        longest_substr = ''
        substr = ''
        N = len(s)

        # Iterate through the string and build substrings until we encounter a duplicate char
        for i, c in enumerate(s):
            substr += c

            # Iterate through the remaining chars in the string to build longest substring without repeating characters
            j = i + 1
            while j < N:
                if s[j] not in substr:
                    substr += s[j]
                else:
                    break
                j += 1

            if len(substr) > len(longest_substr):
                longest_substr = substr
            substr = ''

        # Complexity Analysis
        # Time Complexity O(N^2): Iterating through the string once is O(N), however building the substring and checking for duplicates is also O(N) in the worst case
        # Space Complexity O(N): Worst case is when string has all unique chars which means we are building a substring that is the same length as the input string
        return len(longest_substr)

    
    def lengthOfLongestSubstringOptimized(self, s: str) -> int:
        # Initialize a set to keep track of unique characters in our current window, and two pointers to define the window's boundaries
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is already in our set, we have a duplicate
            # We must shrink our window from the left until the duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the new, unique character to our window's set
            char_set.add(s[right])
            
            # Update the max length found so far
            # The current window size is (right - left + 1)
            if (right - left + 1) > max_length:
                max_length = right - left + 1
        
        # Complexity Analysis
        # Time Complexity O(N): Each character is visited at most twice (once when added to the set and once when removed), resulting in linear time complexity
        # Space Complexity O(min(M, N)): The size of the set is limited by the number of unique characters in the string (M) and the length of the string (N)
        return max_length