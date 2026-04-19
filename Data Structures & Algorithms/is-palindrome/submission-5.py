class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        text = s.lower()
        while left < right:
            while left < right and not text[left].isalnum():
                left += 1
            while left < right and not text[right].isalnum():
                right -= 1
                
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1
        return True
        