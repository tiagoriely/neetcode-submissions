class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for ch in s:

            # Check if the current character is a closing bracket
            if ch in closeToOpen:
                # Check if not empty and if the top stack is an opening bracket
                if stack and stack[-1] == closeToOpen[ch]: # if stack array not empty it returns True
                    stack.pop() # valid pair, remove it
                else:
                    return False # empty stack OR wrong bracket on top
            else:
                stack.append(ch) # opening bracket → push
        
        return not stack

               

        