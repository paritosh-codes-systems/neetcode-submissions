class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}

        for index, number in enumerate(numbers):
            temp_target = target - number
            if temp_target in map:
                return [map[temp_target]+1, index+1]
            
            else:
                map[number] = index
        
        return []
                

        