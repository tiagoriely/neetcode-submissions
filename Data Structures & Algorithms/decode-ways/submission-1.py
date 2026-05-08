class Solution:
    def numDecodings(self, s: str) -> int:
        '''Recursion with Memoization'''
        dp = {len(s): 1}
        
        def dfs(i):
            # Base Case
            if i in dp:
                return dp[i]
            # cannot use '0' on its own
            if s[i] == '0':
                return 0

            count = dfs(i + 1)
            # Count options with 2 characters
            if i < len(s) - 1:
                if (s[i] == '1' or 
                   (s[i] == '2' and s[i + 1] < '7')):
                    count += dfs(i + 2) 
            dp[i] = count
            return count
        
        return dfs(0)