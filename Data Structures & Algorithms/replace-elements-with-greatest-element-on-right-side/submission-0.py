class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # look at the current value and then navigte to right 

        # Iteration 1
        # 2 scan from left and if right > left then overwrite the current index 
        

        for index, num in enumerate(arr):
            if(index+1 == len(arr)):
                arr[index] = -1
            else:
                current_right_max_val = arr[index + 1]
                for right_index, right_num in  enumerate(arr[index + 1:], start=index + 1):
                    current_right_max_val = max(current_right_max_val,right_num )
                arr[index]= current_right_max_val
                
            
            print(arr)
            print("end of first loop" + str(index))

        return arr