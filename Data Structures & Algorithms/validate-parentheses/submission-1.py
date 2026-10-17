class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }


        running_stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                running_stack.append(ch)
            else:
                if len(running_stack) == 0 :
                    return False    
                if valid_pairs[ch] != running_stack[-1]:
                    return False
                else:
                    running_stack.pop()


        if len(running_stack) ==0:
            return True
        
        return False