class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1) # because dp[n] represents the virtual top (finish line)

        # dp[0] and dp[1] are 0 (free starting points), fill from i=2 onwards
        for i in range(2, n + 1):
            # min cost to reach i = cheapest of: (arrive at i-1, pay to leave) or (arrive at i-2, pay to leave)
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n] # minimum cost to reach the top
 