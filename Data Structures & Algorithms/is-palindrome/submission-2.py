class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not any (ch.isalnum() for ch in s):
            return True
        
        s_low = s.lower()
        
        left, right = 0, len(s) - 1
        while left < right:
            while not s_low[left].isalnum():
                left += 1
            while not s_low[right].isalnum():
                right -= 1

            if s_low[left] != s_low[right]:
                print(f"left: {s_low[left]}")
                print(f"right: {s_low[right]}")
                return False
            left += 1
            right -= 1
        return True
        