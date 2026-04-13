# Name: Johnson Dinh
# Time: 10:42
# Language: Python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        # Sort and join strings together to compare if they are the same since anagrams must have the same characters throughout the sequence
        s1 = "".join(sorted(s))
        t1 = "".join(sorted(t))

        if t1 == s1:
            return True

        # Complexity Analysis
        # Time Complexity O(N log N): sorted() algorithm uses Timsort, which takes O(N log N) time, given N is the length of the string
        #                             String comparison at end takes O(N) time, but slower sorting step dictates overall time complexity
        # Space Complexity O(N): sorted() algorithm does not sort the string in place; instead it creates and returns a brand new list of chars
        #                        "".join() method then creates another new string, therefore memory used scales linearly with size of input str
        return False


    def isAnagramOptimized(self, s: str, t: str) -> bool:
        # Early exit if lengths don't match
        if len(t) != len(s):
            return False

        # Build the frequency map for string 's'
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Subtract the frequencies using string 't'
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        # Complexity Analysis
        # Time Complexity O(N): Based on N length of strings, we iterate through `s` and `t` in two separate linear passes
        #                       Since dictionary lookups and insertions in Python are O(1) on average, the overall time complexity scales linearly
        # Space Complexity O(N) or O(1): Generally, strings containing any Unicode character, the worst-case is O(N) 
        #                                because dictionary could theoretically grow linearly with size of a completely unique input str
        #                                If we assume standard constraint of inputs consist only of lowercase English letters, the space complexity
        #                                strictly bounds to O(1)
        return True