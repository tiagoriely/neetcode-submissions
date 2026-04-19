class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        left = 0
        length = 0

        for right in range(len(s)):
            if s[right] in hashMap:
                # never move left backwards
                left = max(hashMap[s[right]] + 1, left)
            
            # Update map with index value
            hashMap[s[right]] = right
            length = max(length, right - left + 1)

        return length
