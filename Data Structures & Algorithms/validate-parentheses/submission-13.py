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
                    # made a mistake here
                    return False

            else:
                stack.append(ch)
        print(stack)

        return not stack