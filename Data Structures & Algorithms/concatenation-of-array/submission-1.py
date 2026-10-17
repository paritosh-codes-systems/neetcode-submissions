class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list()
        counter = 0
        for idx in range(2* len(nums)):
            if(idx == len(nums)):
                counter=0

            ans.append(nums[counter])
            counter = counter +1


        return ans