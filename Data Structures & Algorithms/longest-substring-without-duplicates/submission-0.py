class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Slindin Window Optimal
        hashMp = {}
        left = 0
        size = 0
        
        for right in range(len(s)):
            if s[right] in hashMp:
                # Never move left backwards — only forward
                left = max(hashMp[s[right]] + 1, left)

            hashMp[s[right]] = right
            size = max(size, right - left + 1)

        return size



        