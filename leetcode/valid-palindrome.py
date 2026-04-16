# Name: Johnson Dinh
# Time: 10:24
# Language: Python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Early exit because any length less than 2 automatically implies palindrome, if s is reversed
        if len(s) < 2:
            return True

        # Create new string to store only alphanumeric characters
        t = "".join(c for c in s if c.isalpha() or c.isdigit())
    
        # Set two indices to traverse from from beginning and end separately
        # Check if char in lowercase are the same when iterating from both sides
        i = 0  # Begin index
        j = len(t) - 1  # End index
        while i < j:
            t1 = t[i].lower()
            t2 = t[j].lower()

            if t1 != t2:
                return False

            i += 1
            j -= 1

        # Complexity Analysis
        # Time Complexity O(N): Iterating through a for loop once results in O(N) time; same applies to while loop used. This results
        #                       in O(2N) time which simplifies to O(N) execution time. Thus, execution time scales linearly with input
        #                       size N
        # Space Complexity O(N): Storing a new string from list comprehension allocates a brand new block of memory to store the contents.
        #                        Worst case is when a string has all alpha-numeric characters, so `t` will be the same size as `s`, meaning
        #                        that memory usage scales linearly with the input
        return True
            

    def isPalindromeOptimized(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:
            # Advance 'i' if it's pointing to a non-alphanumeric character
            while i < j and not s[i].isalnum():
                i += 1
                
            # Retreat 'j' if it's pointing to a non-alphanumeric character
            while i < j and not s[j].isalnum():
                j -= 1
                
            # Compare the valid characters (ignoring case)
            if s[i].lower() != s[j].lower():
                return False
                
            # Move both pointers inward for the next comparison
            i += 1
            j -= 1
        
        # Complexity Analysis
        # Time Complexity O(N): Although 2 while loops within 1 while loop looks like O(N^3), we realize that the inner while loops do not
        #                       iterate throughout the entire string. The inner loops stop until the current char is not alpha-numeric.
        #                       Therefore, we need only iterate through the entire string once since these inner loops just speed up the
        #                       incrementation for us, if true. Algorithm runs through each char exactly once, so time complexity is O(N)
        # Space Complexity O(1): In auxiliary space, the algorithm runs in O(1) since we are checking the string in-place and only utilizing
        #                        two integer variables for "pointers". Memory remains strictly constant at O(1) regardless of the size
        return True