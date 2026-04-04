class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}": "{", "]": "[", ")": "("}

        for ch in s:
            print(stack)
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    stack.append(ch)

            else:
                stack.append(ch)
        print(stack)

        return not stack