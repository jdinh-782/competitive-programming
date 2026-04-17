# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0

        for i in range(N - 1):
            buy = prices[i]
            sold = max(prices[i:N])
            
            if sold > buy:
                profit = sold - buy
                if profit > max_profit:
                    max_profit = profit

        # Complexity Analysis
        # Time Complexity O(N^2): Iterating through the array once is O(N), however array slicing is also O(N). Doing this operation
        #                         within the for loop results in O(N^2) runtime since max() also has to scan through all remaining elements
        # Space Complexity O(N): Doing `prices[i:N]` creates a new list in memory which contains the slice of elements. New memory
        #                        is being allocated on every single iteration when performing max()
        return max_profit


    def maxProfitOptimized(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        max_profit = 0
        # Initialize min_price to infinity so the first day always becomes the minimum
        min_price = float('inf') 
        
        for price in prices:
            if price < min_price:
                # We found a new historical low, so we wouldn't sell today. Update our buy price.
                min_price = price
            else:
                # We didn't find a new low, so let's see what our profit would be if we sold today
                current_profit = price - min_price
                
                # Update max_profit if today's profit is the best we've seen
                if current_profit > max_profit:
                    max_profit = current_profit
        
        # Complexity Analysis
        # Time Complexity O(N): We only iterate through the array once and evaluate on the fly
        # Space Complexity O(1): Algorithm only evaluates the array strictly in place. Memory is only allocated for integer variables to hold
        #                        the `min_price` and `max_profit`, which take up a constant amount of memory regardless of input size
        return max_profit