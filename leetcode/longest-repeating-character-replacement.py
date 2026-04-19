# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # If all characters are the same, then s already contains longest repeating character
        if len(set(s)) < 2:
            return len(s)

        max_length = 0
        right = 0
        N = len(s)
        substr = ''
        j = k


        # Initial idea is to iterate the string once and build a substring of repeating characters
        # If we encounter a different character, we can use one of our k replacements to replace it and continue building the substring
        # If we encounter another different character, we can use another replacement, and so on until we run out of replacements
        # At that point, we can check if the length of the current substring is greater than the max length found so far, and then reset the substring and start building a new one from the next character in the string
        for right in range(N):
            substr += s[right]

            while len(set(substr)) != 1:
                if j == 0:
                    substr = substr[:-1]
                
                if j > 0:
                    substr = substr[:-1] + substr[-1]
                    j -= 1

            if j == 0 and len(set(substr)) != 1:
                substr = ''
                j = k

            if len(substr) > max_length:
                max_length = len(substr)

        # Complexity Analysis
        # Time Complexity O(N^2): Iterating through the string once is O(N), however building the substring and checking for duplicates is also O(N) in the worst case
        # Space Complexity O(N): Worst case is when string has all unique chars which means we are building a substring that is the same length as the input string
        return max_length


    def characterReplacementOptimized(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        left = 0
        
        # maxf tracks the highest frequency of a single character in the current window
        maxf = 0
        
        for right in range(len(s)):
            # Add the right character to our frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Update the most frequent character count
            maxf = max(maxf, count[s[right]])
            
            # The magic equation: if we need to replace more than k characters, the window is invalid
            while (right - left + 1) - maxf > k:
                # Remove the left character from our map and shrink the window
                count[s[left]] -= 1
                left += 1
                
            # If the window is valid, check if it's the longest we've seen
            if (right - left + 1) > max_length:
                max_length = right - left + 1
        
        # Complexity Analysis
        # Time Complexity O(N): Each character is visited at most twice (once when added to the count and once when removed), resulting in linear time complexity
        # Space Complexity O(1): The size of the count dictionary is limited by the number of unique characters in the string, which is at most 26 for uppercase English letters
        return max_length