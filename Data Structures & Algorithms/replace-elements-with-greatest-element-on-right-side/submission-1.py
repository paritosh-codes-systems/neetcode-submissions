class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        current_max = -1
        for index in range(n-1, -1, -1):
            temp_max = arr[index]
            arr[index] = current_max 
            current_max = max(temp_max, current_max)
        return arr
    

        
