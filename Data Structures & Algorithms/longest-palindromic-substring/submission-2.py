class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        # Odd length
        for i in range(len(s)):
            R, L = i, i
            while L >= 0 and R < len(s) and s[R] == s[L]:
                if (R - L + 1) > length:
                    length = R - L + 1
                    res = s[L: R + 1]
                L -= 1
                R += 1
        
        # Even length
        for i in range(len(s)):
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[R] == s[L]:
                if (R - L + 1) > length:
                    length = R - L + 1
                    res = s[L: R + 1]
                L -= 1
                R += 1
        return res
        