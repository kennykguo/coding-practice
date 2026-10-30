class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for ch in s:

            if ch == "[" or ch == "(" or ch == "{":
                stack.append(ch)
            
            # rules - must be closed in correct torder
            elif ch == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            
            elif ch == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            
            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        
