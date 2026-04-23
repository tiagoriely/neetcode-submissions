class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        self.backtrackingHelper(0, nums, curSet, subsets)
        return subsets
    
    def backtrackingHelper(self, i, nums, curSet, subsets):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return
        
        # Decision 1: Include nums[i]
        curSet.append(nums[i])
        self.backtrackingHelper(i + 1, nums, curSet, subsets)
        curSet.pop()

        # Decision 2: NOT including nums[i]
        self.backtrackingHelper(i + 1, nums, curSet, subsets)


        