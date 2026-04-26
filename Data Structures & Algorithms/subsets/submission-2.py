class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []

        def dfs_backtracking(i, nums, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            # Decision 1: including nums[i]
            curSet.append(nums[i])
            dfs_backtracking(i + 1, nums, subsets, curSet)
            curSet.pop()

            # Decision: NOT including nums[i]
            dfs_backtracking(i + 1, nums, subsets, curSet)
        
        dfs_backtracking(0, nums, subsets, curSet)

        return subsets

