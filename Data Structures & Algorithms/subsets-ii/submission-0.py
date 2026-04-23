class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Important to sort first
        nums.sort()
        subsets, curSet = [], []

        def dfs_backtracking(i):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            # Decision 1: include nums[i]
            curSet.append(nums[i])
            dfs_backtracking(i + 1)
            curSet.pop()
            
            # Decision 2: NOT including nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs_backtracking(i + 1)

        dfs_backtracking(0)
        return subsets
        