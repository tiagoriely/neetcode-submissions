class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = []
        candidates.sort()

        def backtracking_dfs(i, curComb, total):

            if total == target:
                combs.append(curComb.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            curComb.append(candidates[i])
            backtracking_dfs(i + 1, curComb, total + candidates[i])
            curComb.pop()

            # Skip same values
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtracking_dfs(i + 1, curComb, total)

        backtracking_dfs(0, [], 0)

        return combs
            


            # seen.append(candidates[i])



            


        