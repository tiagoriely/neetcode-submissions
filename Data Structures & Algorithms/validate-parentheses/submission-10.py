class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        if len(s) < 2 or len(s) % 2 != 0:
            return False


        for i in range(len(s)):
            print(stack)

            if s[0] != "{" and  s[0] != "(" and s[0] != "[":
                return False

            if s[i] == "{" or  s[i] == "(" or s[i] == "[":
                stack.append(s[i])

            if len(stack) > 0:
                if s[i] == "}" and stack[len(stack) - 1] != "{":
                    return False
                if s[i] == ")" and stack[len(stack) - 1] != "(":
                    return False
                if s[i] == "]" and stack[len(stack) - 1] != "[":
                    return False

                if s[i] == "}" and stack[len(stack) - 1] == "{":
                    stack.pop()
                if s[i] == ")" and stack[len(stack) - 1] == "(":
                    stack.pop()
                if s[i] == "]" and stack[len(stack) - 1] == "[":
                    stack.pop()
        
        if len(stack) > 0:
            return False        
        return True

        