class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def backtracking_dfs(i, curComb):
            # Important to separate both ifs
            if i > n: # always stop when i bigger
                if len(curComb) == k: # sometimes save when k - size
                    combs.append(curComb.copy())
                return
            
            curComb.append(i)
            backtracking_dfs(i + 1, curComb)
            curComb.pop()
            backtracking_dfs(i + 1, curComb)

        backtracking_dfs(1, [])
        return combs

            



        