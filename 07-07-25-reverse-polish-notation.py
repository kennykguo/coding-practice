class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/": # character is an operator
                token2 = stack.pop()
                token1 = stack.pop()
                if tokens[i] == "+":
                    total = int(token1) + int(token2)
                elif tokens[i] == "-":
                    total = int(token1) - int(token2)
                elif tokens[i] == "*":
                    total = int(token1) * int(token2)
                elif tokens[i] == "/":
                    total = int(token1) / int(token2)
                    total = int(total)
                stack.append(str(total))
                print(stack)
                
            
            else: # add the character
                stack.append(tokens[i])
        
        print(stack)
        return int(stack[0])