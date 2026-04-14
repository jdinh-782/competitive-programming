# Name: Johnson Dinh
# Time: 10:35
# Language: Python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Return `strs` array itself since only one item exists which implies it can always be anagram
        if len(strs) == 1:
            return [strs]

        # Store the sorted version of each str with a list of original str that match the sorted version
        d = {}
        for s in strs:
            sorted_s = "".join(sorted(list(s)))
            if sorted_s not in d:
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        
        # Complexity Analysis
        # Time Complexity O(N * K log K): Iterate through `strs` array N times, where N is length of `strs`
        #                                 For every string, we use sorted() which takes O(K log K) time, for K length of string
        # Space Complexity O(N * K): Worst-case is when every string is unique and not an anagram of any other,
        #                            which causes the dictionary to store N distinct keys, and the values will store all N original strings
        #                            Therefore, memory used scales linearly with total amount of data provided from `strs`
        return list(d.values())