class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #start a counter 
        counter=0
        max_counter = 0
        for num in nums:
            # if num is 1 then increment the counter 
            if num == 1:
                counter = counter +1
                max_counter = max(max_counter, counter)
            elif num ==0 :
                counter = 0 

        return max_counter
            
        