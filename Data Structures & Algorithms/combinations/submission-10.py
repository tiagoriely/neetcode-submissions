class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combs =  []

        def backtracking_dfs(i, curComb):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            
            for j in range(i, n + 1):
                curComb.append(j)
                backtracking_dfs(1 + j, curComb)
                curComb.pop()
            
        backtracking_dfs(1, [])

        return combs
        