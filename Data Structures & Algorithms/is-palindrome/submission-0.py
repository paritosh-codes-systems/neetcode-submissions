class Solution:
    def isPalindrome(self, s: str) -> bool:
        right_counter = len(s) -1
        left_counter = 0

        while left_counter <= right_counter:
            left_char = s[left_counter]
            right_char = s[right_counter]
            if not left_char.isalnum():
                left_counter = left_counter +1
                continue
            if not right_char.isalnum():
                right_counter =right_counter -1
                continue
                
            
            if left_char.lower() == right_char.lower():
                left_counter = left_counter +1
                right_counter =right_counter -1
                continue
            else:
                return False


        return True    
        
        