class Solution:
    def rob(self, nums: List[int]) -> int:
        '''TOUGH ONE FOR ME'''
        cache = {}
        
        if len(nums) == 1:
            return nums[0]
        
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            if (i, flag) in cache:
                return cache[(i, flag)]
            
            cache[(i, flag)] = max(
                dfs(i + 1, flag),                       # skip house i
                nums[i] + dfs(i + 2, flag or i == 0))   # rob house i
            
            return cache[(i, flag)]
        
        return max(dfs(0, True), dfs(1, False)) # max((House 0, excluse last house), (house 1, allow house n-1))
        