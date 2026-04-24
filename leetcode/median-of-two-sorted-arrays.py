# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1)
        N = len(nums2)
        
        sum1 = 0
        if M == 1:
            sum1 = nums1[0]
        else:
            left = 0
            right = M - 1

            while left < right:
                sum1 += nums1[left]
                sum1 += nums1[right]

                left += 1
                right -= 1
        
        sum2 = 0
        if N == 1:
            sum2 = nums2[0]
        else:
            left = 0
            right = N - 1

            while left < right:
                sum2 += nums2[left]
                sum2 += nums2[right]

                left += 1
                right -= 1

        # Avoid division by 0 error
        A = 0
        B = 0
        if M > 0:
            A = sum1 / M
        else:
            return sum2 / N
        
        if N > 0:
            B = sum2 / N
        else:
            return sum1 / M

        res = A + B
        res /= 2

        # Complexity Analysis
        # Time Complexity O(M + N): Where M and N are the lengths of the input lists. This is because we are iterating through both lists once to calculate the sums
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the sums and variables, regardless of the input size
        return res


    def findMedianSortedArraysOptimized(self, nums1: list[int], nums2: list[int]) -> float:
        # We always want to binary search the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        # The total number of elements that should be on the left side of our cuts
        half_len = (m + n + 1) // 2
        
        while left <= right:
            # i is the partition cut in nums1
            i = left + (right - left) // 2
            # j is the perfectly balancing partition cut in nums2
            j = half_len - i
            
            # Extract the 4 boundary values surrounding our cuts
            # Use -infinity and infinity to handle cuts that fall on the absolute edges
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # The Cross-Check: Is the left side truly smaller than the right side?
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                
                # If total length is odd, the median is just the biggest number on the left
                if (m + n) % 2 == 1:
                    return float(max(nums1_left, nums2_left))
                
                # If even, it's the average of the biggest on the left and smallest on the right
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
                
            # The cut in nums1 is too far right, so search left
            elif nums1_left > nums2_right:
                right = i - 1
            # The cut in nums1 is too far left, so search right
            else:
                left = i + 1

        # Complexity Analysis
        # Time Complexity O(log(min(M, N))): Where M and N are the lengths of the input lists. This is because we are performing a binary search on the smaller list
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables, regardless of the input size
        return 0