# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # If `nums` array only has 2 elements and we can't multiply element at index, then result must be inverse of `nums`
        if len(nums) == 2:
            return nums[::-1]

        # Iterate through length of array, and perform calculation throughout the array itself, while checking if indices are same
        i = 0
        N = len(nums)
        answer = []

        while i < N:
            result = 1

            for j in range(0, len(nums)):
                if j != i:
                    if nums[j] == 0:
                        result = 0
                        break
                    else:
                        result *= nums[j]
            
            answer.append(result)
            i += 1

        # Complexity Analysis
        # Time Complexity O(N^2): Due to the while loop iterating N times + for loop iterating N times, code performs roughly N X N = N^2 times
        # Space Complexity O(1): Creating an `answer` array of size N results in memory used with O(1) auxiliary space (or O(N) total space)
        return answer


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # If `num` array only has 2 elements and we can't multiply element at index, then result must be inverse of `nums`
        if len(nums) == 2:
            return nums[::-1]

        N = len(nums)

        # Initialize the answer array with 1s
        answer = [1] * N
        
        # Pass 1: Calculate all the "Left" products
        # answer[i] will store the product of all elements to the left of nums[i]
        left_product = 1
        
        # answer[0] = 1
        # left_product = 1 * 1 = 1
        # answer[1] = 1
        # left_product = 1 * 2 = 2
        # answer[2] = 2
        # left_product = 2 * 3 = 6
        # answer[3] = 6
        # left_product = 6 * 4 = 24
        for i in range(N):
            answer[i] = left_product  
            left_product *= nums[i]
            
        # Pass 2: Calculate all the "Right" products on the fly
        # Multiply the existing left product in answer[i] by the running right_product
        right_product = 1

        # answer[3] = 6 * 1 = 6
        # right_product = 1 * 4 = 4
        # answer[2] = 2 * 4 = 8
        # right_product = 4 * 3 = 12
        # answer[1] = 1 * 12 = 12
        # right_product = 12 * 2 = 24
        # answer[0] = 1 * 24 = 24
        # right_product = 24 * 1 = 24
        for i in range(N - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
            
        # Complexity Analysis
        # Time Complexity O(N): Performing two independent for loops that pass over the array results in execution time scaling linearly with the input size, i.e. O(2N) -> O(N)
        # Space Complexity O(1): Only utilizing two integer variables to calculate prefix and suffix values while storing results in a singular `answer` array to return
        return answer