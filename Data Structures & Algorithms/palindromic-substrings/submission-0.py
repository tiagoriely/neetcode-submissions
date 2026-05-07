class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        

        for i in range(len(s)):
            # Palindromes of odd sizes
            L, R = i, i
            while (L >= 0 and R < len(s) and 
                   R - L + 1 > 0 and s[L] == s[R]):
                count += 1
                L -= 1
                R += 1
            
            # Palindromes of even sizes
            L, R = i, i + 1
            while (L>= 0 and R < len(s) and 
                   R - L + 1 > 1 and s[L] == s[R]):
                count += 1
                L -= 1
                R += 1

        return count

        