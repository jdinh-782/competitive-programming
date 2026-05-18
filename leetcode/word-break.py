# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # dp[i] means: "Can the substring s[i:] be broken into dictionary words?"
        # We need len(s) + 1 to account for the "empty string" base case at the end
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # Base case: reaching the end means a successful break
        
        # Traverse backwards from the end of the string
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # 1. Ensure the word fits within the remaining length of the string
                # 2. Check if the substring actually matches the word
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    # If it matches, the current index inherits the validity of the index AFTER the word
                    dp[i] = dp[i + len(word)]
                
                # Early Exit: If we found ANY word that successfully connects,
                # we know this index is True. We don't need to check other words.
                if dp[i]:
                    break

        # Complexity Analysis
        # Time Complexity O(N * M * L): The outer loop runs N times. Inner loop iterates through M words. Inside that loop, Python's substring slicing and string comparison
        #                               (`s[i : i + len(word)] == word`) takes up to O(L) time
        # Space Complexity O(N): By utilizing an iterative bottom-up approach, we completely bypass the recursive Call Stack. Memory footprint is dictated by the localized 1D `dp` array on the
        #                        heap, which allocates exactly N + 1 boolean values
        return dp[0]