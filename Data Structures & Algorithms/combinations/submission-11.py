class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def backtracking_dfs(i, curComb):
            if i > n + 1:
                return
            
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            
            # Decision 1: Including i
            curComb.append(i)
            backtracking_dfs(i + 1, curComb)
            curComb.pop()

            # Decision 2: Not including i
            backtracking_dfs(i + 1, curComb)
        
        backtracking_dfs(1, [])

        return combs


        