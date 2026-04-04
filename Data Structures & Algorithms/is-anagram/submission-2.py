class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            # A) countS.get(s[i], 0) — retrieves the current stored value for key s[i], 
            #    and returns 0 if the key doesn't exist yet
            # B) the '1' increments that value by 1 
            #    each time the letter is encountered
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        