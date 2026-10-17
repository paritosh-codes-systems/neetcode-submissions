class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #start a counter 
        counter=0
        max_counter = 0
        for num in nums:
            # if num is 1 then increment the counter 
            if num == 1:
                counter = counter +1 
            elif num ==0 :
                if counter > max_counter:
                    max_counter = counter 
                counter = 0 

            if counter > max_counter:
                max_counter = counter 

        return max_counter
            
        