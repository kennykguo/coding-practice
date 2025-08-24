class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True

        for char in s:

            if char == ')':
                if  not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()         
            else:
                stack.append(char)
        
        return len(stack) == 0

            