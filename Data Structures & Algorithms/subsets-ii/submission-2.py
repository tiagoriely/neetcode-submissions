class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []

        def dfs_backtracking(i, nums, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            
            
            # Decision 1: Including nums[i]
            curSet.append(nums[i])
            dfs_backtracking(i + 1, nums, subsets, curSet)
            curSet.pop()

            # Decision 2: NOT including nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs_backtracking(i + 1, nums, subsets, curSet)
            

        dfs_backtracking(0, nums, subsets, curSet)

        return subsets
        