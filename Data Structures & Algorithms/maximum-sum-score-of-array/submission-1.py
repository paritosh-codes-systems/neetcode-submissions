class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate the sum of the entire array once
        left_sum = 0
        max_score = float('-inf')  # Initialize with negative infinity to handle negative values safely
        
        for num in nums:
            left_sum += num  # Maintain running sum from index 0 to i
            
            # The suffix sum from index i to end is: total_sum - prefix_sum_before_i
            # Which is mathematically equivalent to: total_sum - left_sum + num
            right_sum = total_sum - left_sum + num
            
            # Capture the maximum score encountered so far
            current_score = max(left_sum, right_sum)
            if current_score > max_score:
                max_score = current_score
                
        return max_score