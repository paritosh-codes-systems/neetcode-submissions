class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True

        if len(set(nums)) != len(nums):
            return False

        if  max(nums) - min(nums) + 1 == len(nums):
            return True

        return False