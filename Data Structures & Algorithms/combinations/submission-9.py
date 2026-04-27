class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        optimal recursive solution
        '''
        combs = []

        def backtracking_dfs(i, curComb):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            
            # Optimisation here
            for j in range(i, n + 1):
                curComb.append(j)
                backtracking_dfs(j + 1, curComb)
                curComb.pop()


        backtracking_dfs(1, [])

        return combs        

        '''
        backtracking_dfs(1, [])
            j=1 → append 1 → [1]
                j=2 → append 2 → [1,2] ✅ SAVE (len==k, return)
                j=3 → append 3 → [1,3] ✅ SAVE
                j=4 → append 4 → [1,4] ✅ SAVE
            j=2 → append 2 → [2]
                j=3 → append 3 → [2,3] ✅ SAVE
                j=4 → append 4 → [2,4] ✅ SAVE
            j=3 → append 3 → [3]
                j=4 → append 4 → [3,4] ✅ SAVE
            j=4 → append 4 → [4]
                (no j left) → returns nothing
    '''    



        