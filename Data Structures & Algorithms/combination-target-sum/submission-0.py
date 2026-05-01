class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        
        
        def backtracking_dfs(i, curComb, total):
            if total == target:
                combs.append(curComb.copy())
                return
            if  i >= len(nums) or total > target:
                return
            
            # Decision 1 - Including nums[i]
            curComb.append(nums[i])
            backtracking_dfs(i, curComb, total + nums[i]) # Incrementing total
            curComb.pop()

            # Decision - Not including nums[i]
            backtracking_dfs(i + 1, curComb, total) # Incrementing to next value

        backtracking_dfs(0, [], 0)

        return combs



        