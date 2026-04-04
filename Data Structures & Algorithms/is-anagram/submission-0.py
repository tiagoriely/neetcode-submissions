class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap_s = {}
        countMap_t = {}

        for letter in s:
            if letter not in countMap_s:
                countMap_s[letter] = 1
            else:
                countMap_s[letter] += 1
        
        for letter in t:
            if letter not in countMap_t:
                countMap_t[letter] = 1
            else:
                countMap_t[letter] += 1

        if countMap_s == countMap_t:
            return True
        return False

        