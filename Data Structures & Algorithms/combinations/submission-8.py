class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def backtracking_dfs(i, n, curComb):
            if i > n:
                if len(curComb) == k:
                    combs.append(curComb.copy())
                return
            
            # Decision 1
            curComb.append(i)
            backtracking_dfs(i + 1, n, curComb)
            curComb.pop()

            # Decision 2: Not including i
            backtracking_dfs(i + 1, n, curComb)

        backtracking_dfs(1, n, [])

        return combs        


            



        