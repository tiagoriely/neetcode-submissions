class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs_memoization(i):
            if i >= n:
                return i == n
            if i in cache:
                return cache[i]
            cache[i] = dfs_memoization(i + 1) + dfs_memoization(i + 2)
            return cache[i]
        
        return dfs_memoization(0)
        