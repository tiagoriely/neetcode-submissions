class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        i = 0
        while i < n - 1:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1

        return dp[1]
            
        