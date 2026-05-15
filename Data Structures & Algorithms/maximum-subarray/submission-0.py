class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''Brute Force O(n^2)'''
        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
        return maxSum

        