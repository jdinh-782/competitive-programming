# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        if len(s) < len(t):
            return ""

        d = {}
        for c in t:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        result = ""
        window = ""
        for c in s:
            if len(window) == 0:
                if c in d:
                    window += c
            else:
                window += c

            if c in d:
                d[c] -= 1
            
                # Each time we decrement count, check if all keys have values <= 0
                finished = all(val <= 0 for val in d.values())
                if finished:
                    if result == "":
                        result = window
                    else:
                        if len(window) < len(result):
                            result = window
                    
                    # Reset d
                    d = {}
                    for c in t:
                        if c not in d:
                            d[c] = 1
                        else:
                            d[c] += 1

                    # Reset window
                    window = ""
        
        # Complexity Analysis
        # Time Complexity O(N * M): We iterate through the string s (N) and for each character, we check if all values in d are <= 0 which takes O(M) time where M is the 
        #                           number of unique characters in t
        # Space Complexity O(N + M): In the worst case, we could be building a window that is the same length as s, and we also have to store the frequency of characters in t 
        #                            which takes O(M) space where M is the number of unique characters in t
        return result


    def minWindowOptimized(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""

        # Dictionary to keep track of required character counts
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        # Dictionary to keep track of counts in our current window
        window = {}
        
        # 'need' is total unique characters in t
        # 'have' is how many unique characters are currently satisfied in the window
        have, need = 0, len(count_t)
        
        # Store the result as pointers (left, right) to avoid string copying, and the min length
        res = [-1, -1]
        res_len = float("infinity")
        
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # If the character is useful and we hit the exact required count, increment 'have'
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # When the window is valid, try to shrink it from the left
            while have == need:
                # 1. Update our result if this window is smaller than the previous best
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)

                # 2. Shrink the window by removing the left character
                left_char = s[left]
                window[left_char] -= 1
                
                # 3. If removing this character breaks our valid state, decrement 'have'
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                # Move the left pointer up
                left += 1

        # Return the sliced string using our saved pointers, or "" if no valid window was found
        left_idx, right_idx = res

        # Complexity Analysis
        # Time Complexity O(N): We iterate through the string s once (N) and each character is added and removed from the window at most once, resulting in linear time complexity
        # Space Complexity O(1): The dictionaries `count_t` and `window` will at most store counts for all unique characters in t, which is limited to 26 lowercase letters, resulting in constant space complexity
        return s[left_idx : right_idx + 1] if res_len != float("infinity") else ""