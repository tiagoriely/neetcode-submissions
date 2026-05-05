class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0;
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]                 # best house to rob from houses [0]
        dp[1] = max(nums[0], nums[1])   # best house to rob from houses [0..1]

        for i in range(2, len(nums)):
            # best house to rob from houses [0..i]
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1] # best I can rob from all houses [0..n-1]