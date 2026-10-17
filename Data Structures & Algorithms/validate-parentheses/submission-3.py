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
                if not running_stack :
                    return False    
                if valid_pairs[ch] != running_stack[-1]:
                    return False
                else:
                    running_stack.pop()


        if not running_stack:
            return True
        
        return False